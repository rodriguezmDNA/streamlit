# from SuppSmartFunctions import * 
# from upgrade_querySearch import *
import streamlit as st

############################################################
###### testing grounds
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import streamlit as st

stop_words = stopwords.words('english')
extraStop = ["mg", "erowid", "-PRON-", "june", 'i知']
stop_words.extend(extraStop)

try:
    import spacy
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
except Exception as e:
    st.write(f"Error loading spaCy model: {e}")
    
#import spacy #Language model
#nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner']) 
############################################################





############################################################


import pydantic

# Display the version in Streamlit
from importlib.metadata import version, PackageNotFoundError

#st.write(f"spacy version: {version("spacy")}")
v = version("pydantic")
st.write(f"pydantic version: {v}")
v = version("spacy")
st.write(f"spacy version: {v}")

try:
    typing_extensions_version = version("typing_extensions")
except PackageNotFoundError:
    typing_extensions_version = "typing_extensions is not installed"

st.write(f"typing_extensions version: {typing_extensions_version}")

############################################################


st.image("suppsmart_banner.jpg", use_column_width=True)
st.subheader('Getting smart about dietary supplements')

st.markdown('\n\n')
#st.markdown('\t enter your query:')
query = st.text_input('enter your query: \n (pro tip - a longer, more descriptive query works best!',
	'I want something to help me sleep')
topN = st.text_input('limit your search to top results', 3)
topN = int(topN)




st.write(topN*2)
st.write(stop_words[-10:])

# supReq = False

# if st.button("'supp me"):
# 	recList, recTable,searchQuery = wrapperSimilarSupplements(query,topN)
# 	st.table(recList)
# 	supReq = True

# 	#st.pyplot( plotCosinSim(recTable))



# st.markdown('\n\n\n\n')
# st.subheader('explore what people have said')

# supp = st.selectbox("Choose a supplement", list(scrappedCleanTopic.keys()), 0)
# nTopics = st.slider('Number of topics', 8, 20, 10) 


# if st.button("explore topics"):
# 	###
# 	resMod, resI2W, resCorpus = buildTopicModel(supp,ngram="quad",nTopics=nTopics,modelType="lda")
# 	resTopics = dict(resMod.print_topics())
# 	resTopicsDF = prepDF(resTopics)
# 	plttitle = "most representative words for " + supp + "\n("+str(resTopicsDF.shape[0]) + " topics)"
# 	sns.set(font_scale = 0.8)
# 	sns.heatmap(resTopicsDF.T,cmap="Blues",square=True,cbar_kws={'label':'word importance',"shrink": .5}).set_title(plttitle)
# 	plt.xticks(rotation=45)
# 	st.pyplot()



# # if st.button("explore topics"):
# # 	resLDA, resI2W, resCorp = buildTopicModel(sugSupp,"tri",nTopics,"lda")
# # 	tmpTopics = [list(dict(resLDA.show_topic(_)).keys()) for _ in range(nTopics)]
# # 	tmpTopics = ["".join(str(term)) for term in tmpTopics]
# # 	st.table(tmpTopics)

# # # 	#topicModelSupp(sup,nTopics)) #works well, new tab
# # # 	#st.pyplot(topicModelSupp("Tryptophan",nTopics))
# # # 	#st.markdown(topicModelSupp(supp,nTopics)) #not great
# # # 	#plt.show()


# # st.markdown('')			 
# # st.markdown('_This supplement explorer is a work of Data Science._')
# # st.markdown('It is not intended as a substitute for medical expertise. \
# # 			 Consult a physician, registered dietician or other healthcare professional. \
# # 			 The results here should not be taken as an indication or suggestion of any supplement as safe or effective.')

