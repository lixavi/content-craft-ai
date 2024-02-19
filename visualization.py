import matplotlib.pyplot as plt

def visualize_data(data):
    # Plotting word frequency distribution
    word_freq = get_word_frequency(data)
    plot_word_frequency(word_freq)

def get_word_frequency(data):
    # Count word frequency
    word_freq = {}
    for word in data.split():
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def plot_word_frequency(word_freq):
    # Plotting word frequency distribution
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    top_words = [item[0] for item in sorted_word_freq[:10]]
    top_freq = [item[1] for item in sorted_word_freq[:10]]

    plt.figure(figsize=(10, 6))
    plt.bar(top_words, top_freq, color='skyblue')
    plt.title('Top 10 Most Frequent Words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.show()
