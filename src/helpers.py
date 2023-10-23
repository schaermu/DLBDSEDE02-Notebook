from collections import Counter
from matplotlib import pyplot as plt
import pandas as pd
import gensim
import matplotlib.pyplot as plt
from gensim.models import LsiModel, LdaMulticore, CoherenceModel


# clean up spacy docs
def tidy_tokens(docs):
    cols = [
        "msg_id",
        "token",
        "token_order",
        "lemma",
        "ent_type",
        "tag",
        "dep",
        "pos",
        "is_stop",
        "is_alpha",
        "is_digit",
        "is_punct",
    ]

    meta_df = []
    for ix, doc in enumerate(docs):
        meta = [
            (
                i.text,
                i.i,
                i.lemma_,
                i.ent_type_,
                i.tag_,
                i.dep_,
                i.pos_,
                i.is_stop,
                i.is_alpha,
                i.is_digit,
                i.is_punct,
            )
            for i in doc
            if i.text.strip()
        ]
        meta = pd.DataFrame(meta)
        meta.columns = cols[1:]
        meta = meta.assign(msg_id=ix).loc[:, cols]
        meta_df.append(meta)

    return pd.concat(meta_df)


# get simple word frequency across corpus
def get_word_freq(corpus, dict):
    word_freq = Counter()
    for doc in corpus:
        for word, score in doc:
            word_freq[dict[word]] += score
    return word_freq


# https://stackoverflow.com/a/63032961/221217
def plot_word_freq(tf: Counter, most_common: int = 20):
    y = [count for _, count in tf.most_common(most_common)]
    x = [tag for tag, _ in tf.most_common(most_common)]

    plt.bar(x, y, color="crimson")
    plt.title("Term frequencies")
    plt.ylabel("Frequency")
    plt.xticks(rotation=90)
    for i, (_, count) in enumerate(tf.most_common(most_common)):
        plt.text(
            i,
            count,
            f"{round(count, 2)}",
            rotation=90,
            ha="center",
            va="top" if i < most_common else "bottom",
            color="white" if i < most_common else "black",
        )
    plt.xlim(-0.6, len(x) - 0.4)
    plt.tight_layout()
    plt.show()


def get_specific_topics(model, num_words=5):
    specific_topics = {}
    for topic_id in range(model.num_topics):
        if isinstance(model, gensim.models.LdaModel):
            terms = model.get_topic_terms(topic_id, num_words)
            specific_topics[topic_id] = [
                (model.id2word[term[0]], term[1]) for term in terms
            ]
        else:
            terms = model.show_topic(topic_id, num_words)
            specific_topics[topic_id] = [(term[0], term[1]) for term in terms]
    return specific_topics


def compute_coherence_values(
    dict, corpus, model_type, training_set, stop, coherence="c_v", start=2, step=3
):
    coherence_values = []
    model_list = []
    for num_topics in range(start, stop, step):
        # generate model and store coherence score
        if model_type == "lsi":
            model = LsiModel(corpus, num_topics=num_topics, id2word=dict)
        elif model_type == "lda":
            model = LdaMulticore(
                corpus, num_topics=num_topics, id2word=dict, passes=10, workers=6
            )
        model_list.append(model)
        # get coherence score using cross-validation set
        coherencemodel = CoherenceModel(
            model=model,
            texts=training_set if coherence != "u_mass" else None,
            corpus=corpus if coherence == "u_mass" else None,
            dictionary=dict,
            coherence=coherence,
        )
        coherence_values.append(coherencemodel.get_coherence())
    return model_list, coherence_values


# plot coherence scores to determine optimal topic count visually
def plot_coherence_graph(coherence_values, start, stop, step):
    # Show graph
    x = range(start, stop, step)
    plt.plot(x, coherence_values)
    plt.xlabel("Number of Topics")
    plt.ylabel("Coherence score")
    plt.legend(("coherence_values"), loc="best")
    plt.show()
