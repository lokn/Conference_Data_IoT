import pandas as pd
from collections import Counter


# Load the data from the uploaded CSV file
file_path = './data.csv'
data = pd.read_csv(file_path, delimiter=';')

###
### Research question B
###

# Create a new column to check if the conference country matches the country of the first author
data['match'] = data['Conference country'] == data['Country of first author (as per publication date)']

# Calculate the number of matches and total entries
match_count = data['match'].sum()
total_entries = len(data)

# Calculate the percentage of matches
match_percentage = (match_count / total_entries) * 100

print(match_count, total_entries, match_percentage)

# Create a new dataframe to analyze frequency of country combinations
country_combinations = data[['Conference country', 'Country of first author (as per publication date)']]
country_combinations_count = country_combinations.value_counts().reset_index(name='Count')

print(country_combinations_count)

###
### C 
###

# Calculate the Pearson correlation coefficient
correlation = data['Number of references provided in the PDF'].corr(data['Number of citations under Google Scholar'])

###
### D
###

# Calculate the Pearson correlation coefficient
correlation = data['Number of authors'].corr(data['Number of citations under Google Scholar'])

###
### E
###

# Drop rows where keywords are NaN and then combine all keyword strings into a single list
keywords_series = data['Keywords provided in PDF'].dropna()
keywords_list = keywords_series.str.lower().str.split(', ').sum()  # Split keywords and flatten list

# Count occurrences of each keyword
keyword_counts = Counter(keywords_list)

# Convert the counter to a DataFrame for better visualization
keyword_counts_df = pd.DataFrame(keyword_counts.items(), columns=['Keyword', 'Count']).sort_values(by='Count', ascending=False)

# Display the top 10 most common keywords
print(keyword_counts_df)

###
### Wordcloud
###

# Updated dictionary of word frequencies
updated_word_freq = {
    'Internet of Things': 7,
    'LoRaWAN': 5,
    'RFID': 3,
    'Intermittent Computing': 2,
    'Testbed': 2,
    'Scalability': 2,
    'Wireless Sensing': 2,
    'Neural Networks': 2
}

# Create the word cloud with the updated frequencies
updated_wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(updated_word_freq)

# Display the updated word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(updated_wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axes
plt.title("Word Cloud of Updated Keyword Frequencies")
plt.show()
