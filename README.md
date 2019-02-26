# Quotes generator and [Twitter](https://twitter.com/DeepInspiratio1) bot

OPENAI generated a lot of talk when they revealed they managed to train a  [*"large-scale unsupervised language model which generates coherent paragraphs of text, achieves state-of-the-art performance on many language modeling benchmarks, and performs rudimentary reading comprehension, machine translation, question answering, and summarization — all without task-specific training."*](https://blog.openai.com/better-language-models/).   
They annouced they would not release the dataset, code or the model weights, releasing this information has been a common practice, because *"concerns about large language models being used to generate deceptive, biased, or abusive language at scale"*. I don't agree with the excuse but its true that the model managed to create coeherent text, this was one of the first time i saw a language model managing to do it.     
There is probably some cherry picking of the best samples but this made me want to play with text generators.
Since the model and weights are not released and i don´t have the resources to try to do the same as OpenAI i had to use what´s available from others researchers.   
I decided to use the [ULMFiT model](https://arxiv.org/abs/1801.06146) that is implemented in the [Fastai library](https://www.fast.ai/) to create "inspirational" quotes. Quotes are generaly shorter than full articles so i was hoping to be able to create some coherent text.   
After some strugle the text started to finally make sense, **sometimes**.   
I manually select the best quotes and they are published to twitter you can see them **[here](https://twitter.com/DeepInspiratio1)**    




## Steps
- The first step getting the dataset, i found this [this one with enough quotes](https://www.researchgate.net/publication/304742521_CSV_dataset_of_76000_quotes_suitable_for_quotes_recommender_systems_or_other_analysis) 
- The data exploration of the dataset is in [this notebook](exploration.ipynb)
- Tried to generate quotes but the results were [not good](generator_failure.ipynb)
- Decided to create my own dataset and work with only "inspirational" quotes. I built a web scrapper to get the quotes from the site goodreads, [web scrapper](quotes_scrapping.ipynb)
- tried again to generate text with this new dataset and after some failures it started to make some sense, [clean version](quotes_generator_clean_model.ipynb). it created quotes like  *be strong enough to bear the lessons that come if you learn to love yourself*
- [A notebook](generate_save_quotes.ipynb) loads the model, generates quotes giving a seed and saves them to files
- The best quotes are selected by me manually, in the future, with enough data, will build a NN to deal with this
- Finally i built a [script](twitter_bot.py) that gets a quote from the selected ones and publishes it automatically to twitter
- Upload it and set a task to run automatically every day to post a tweet

It was an interesting project, will work on improving the quality of the generated text
