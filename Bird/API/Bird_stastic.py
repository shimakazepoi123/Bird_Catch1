from pyecharts.charts import WordCloud, Bar
import datetime

FILE_NAME = 'WordCloud ' + str(datetime.datetime.now())


# create wordcloud
def wordcloud_create(stastic, series_name='鸟种记录'):
    (
        WordCloud()
            .add(series_name=series_name, data_pair=stastic, word_size_range=(5, 60))
            .render('Stastic/{0}.{1}'.format(FILE_NAME, '.html'))
    )
