from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
content = "TEAM ELITERATE is India's largest Educational destination, loved by thousands of aspirants across the country. Through our website, we help many students who are preparing actively for various exams & score better. We have established & nurtured highly engaging exam-specific communities of students and mentors for more than 1300 exams with 43000+ MockTests.The E-LITERATE community lets users collectively Compete each other through mock tests at a national level. "
wordcloud = WordCloud(width=800, height=800, background_color="white",min_font_size = 10).generate(content)
plt.figure(figsize = (8,8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
