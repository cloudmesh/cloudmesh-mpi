# Survey of different NLP services and their features

## Introduction

There exist a multitude of APIs available that offer natural langauge processing services with pre-packaged, trained functions. This document will act as a survey for a number of these different services, highlighting their features and similarities.

- Amazon Comprehend (available through AWS)
- Azure Cognitive Science for Language
- Google Natural Language API
- Salesforce Einstein Language
- IBM Watson Natural Language Understanding


## Overview

The following chart shows the most common features that are shared among APIs and links to the specific corresponding functions in their documentation.

|   | Amazon Comprehend  | Azure  | Google  | Einstein Language  | IBM Watson  |
|---|---|---|---|---|---|
| Sentiment detection  | DetectSentiment [^aws-comprehend-sentiment] | sentiment [^azure-language-sentiment]  | analyzeSentiment [^google-natural-language-sentiment] | CommunitySentiment [^einstein-language-sentiment]  | Sentiment [^ibm-natural-language-sentiment]  |
|  Keyphrase extraction | DetectKeyPhrases [^aws-comprehend-keyphrase]  | keyPhrases [^azure-language-keyphrase]  | ---  | ---  | Keywords [^ibm-natural-language-keyphrase] |
|  Syntax detection | DetectSyntax [^aws-comprehend-syntax]  | --- | analyzeSyntax [^google-natural-language-syntax]  | ---  | Syntax [^ibm-natural-language-syntax]  |
|  Entity recognition | DetectEntities [^aws-comprehend-entity]  |  entities/recognition/general [^azure-language-entity] | analyzeEntities [^google-natural-language-entity] | ---  | Entities [^ibm-natural-language-entity]  |
|  Language detection | DetectDominantLanguage [^aws-comprehend-language]  | languages [^azure-language-language]  | (included in others)  |  --- | (included in others)  |
|  PII detection | DetectPiiEntities [^aws-comprehend-pii]  | entities/recognition/pii [^azure-language-pii]  | ---  | ---  | ---  |

## Amazon Comprehend [^aws-comprehend]

Supported Interfaces:
AWS CLI, Python, Java

### Functions

The following is a non-exhaustive selection of functions provided by the API 

DetectSentiment [^aws-comprehend-sentiment]
- language, text -> Sentiment [POSITIVE | NEGATIVE | NEUTRAL | MIXED], SentimentScore [float 0.0-1.0 for each possible sentiment]

DetectKeyPhrases [^aws-comprehend-keyphrase]
- language, text -> list of key phrases with confidence score and location in text

DetectSyntax [^aws-comprehend-syntax]
- language, text -> list of tokenized elements of the input text, each with a declared part of speech

DetectEntities [^aws-comprehend-entity]
- custom endpoint model (optional), language, text -> list of detected entities with type, score, and location

DetectDominantLanguage [^aws-comprehend-language]
- text -> language code, score

DetectPiiEntities [^aws-comprehend-pii]
- language, text -> list of entities with type, score

## Azure Cognitive Science for Language [^azure-language]

Supported Interfaces:
REST API, Python, C#, Java, Javascript

### Functions

sentiment [^azure-language-sentiment]
- document, key, endpoint -> sentiment scores [positive, negative, neutral] for entire input as well as each sentence 

keyPhrases [^azure-language-keyphrase]
- document, key, endpoint -> list of keyphrases, warnings, errors

entities/recognition/general [^azure-language-entity]
- document, key, endpoint -> list of recognized entities with their category, subcategory, and score

languages [^azure-language-language]
- document, key, endpoint -> language name, code, and score

entities/recognition/pii [^azure-language-pii]
- document, key, endpoint -> detected PII with type, location, and score

## Google Natural Language API [^google-natural-language]

Supported Interfaces:
REST API, Python, C#, JAVA, Go, Node.js, PHP, Ruby

### Functions

analyzeSentiment [^google-natural-language-sentiment]
- document, encodingType -> Sentiment object, language, sentences list (each with their own sentiment)

analyzeSyntax [^google-natural-language-syntax]
- document, encodingType -> sentences list, tokens list, language

analyzeEntities [^google-natural-language-entity]
- docuent, encodingType -> entities list, language

## Salesforce Einstein Language [^einstein-language]

Supported Interfaces:
REST API

### Functions

CommunitySentiment [^einstein-language-sentiment]
- document, auth token, cache control, model -> label [positive, negative, neutral], probability scores

## IBM Watson Natural Language Understanding [^ibm-natural-language]

Supported Interfaces:
Rest API, Python, Java, Node, Go, .NET, Ruby, Swift, Unity

### Functions

Sentiment [^ibm-natural-language-sentiment]
- text/url, target keywords -> label, score for document & any target keywords

Keywords [^ibm-natural-language-keyphrase]
- text/url, max # keywords, sentiment/emotion flags -> list of keywords, each with detected sentiment and emotion if flagged

Syntax [^ibm-natural-language-syntax]
- text/url, sentences flag, optional tokens -> detected part of speech, location, and additonal tokens for each word + sentence (if flagged)

Entities [^ibm-natural-language-entity]
- text/url, max # entities, sentiment/emotion/mentions flags -> list of entities with detected labels & additional optional flags

# Bibtex

@misc{aws-comprehend,
	title = {{Natural Language Processing {\textendash} Amazon Comprehend {\textendash} Amazon Web Services}},
	journal = {Amazon Web Services, Inc},
	year = {2021},
	month = {Oct},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://aws.amazon.com/comprehend}
}

@misc{aws-comprehend-sentiment,
	title = {{DetectSentiment - Amazon Comprehend}},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectSentiment.html}
}

@misc{aws-comprehend-keyphrase,
	title = {{DetectKeyPhrases - Amazon Comprehend}},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectKeyPhrases.html}
}

@misc{aws-comprehend-syntax,
	title = {{DetectSyntax - Amazon Comprehend}},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectSyntax.html}
}

@misc{aws-comprehend-entity,
	title = {{DetectEntities - Amazon Comprehend}},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectEntities.html}
}

@misc{aws-comprehend-language,
	title = {{DetectDominantLanguage - Amazon Comprehend}},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectDominantLanguage.html}
}

@misc{aws-comprehend-pii,
	title = {{DetectPiiEntities - Amazon Comprehend}},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectPiiEntities.html}
}

@misc{azure-language,
	author = {aahill},
	title = {{Azure Cognitive Service for language documentation - Tutorials, API Reference - Azure Cognitive Services}},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.microsoft.com/en-us/azure/cognitive-services/language-service}
}

@misc{azure-language-sentiment,
	author = {aahill},
	title = {{Quickstart: Use the Sentiment Analysis client library and REST API - Azure Cognitive Services}},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/sentiment-opinion-mining/quickstart?pivots=rest-api}
}

@misc{azure-language-keyphrase,
	author = {aahill},
	title = {{Quickstart: Use the Key Phrase Extraction client library - Azure Cognitive Services}},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/key-phrase-extraction/quickstart?pivots=rest-api}
}

@misc{azure-language-entity,
	author = {aahill},
	title = {{Quickstart: Use the NER client library - Azure Cognitive Services}},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/named-entity-recognition/quickstart?pivots=rest-api}
}

@misc{azure-language-language,
	author = {aahill},
	title = {{Quickstart: Use the Language Detection client library - Azure Cognitive Services}},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/language-detection/quickstart?pivots=rest-api}
}

@misc{azure-language-pii,
	author = {aahill},
	title = {{Quickstart: Detect Personally Identifying Information (PII) in text - Azure Cognitive Services}},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/personally-identifiable-information/quickstart?pivots=rest-api}
}

@misc{google-natural-language,
	title = {{Cloud Natural Language {$\vert$} Google Cloud}},
	journal = {Google Cloud},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.google.com/natural-language}
}

@misc{google-natural-language-sentiment,
	title = {{Method: documents.analyzeSentiment {$\vert$} Cloud Natural Language API}},
	journal = {Google Cloud},
	year = {2019},
	month = {Dec},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSentiment}
}

@misc{google-natural-language-syntax,
	title = {{Method: documents.analyzeSyntax {$\vert$} Cloud Natural Language API}},
	journal = {Google Cloud},
	year = {2019},
	month = {Dec},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSyntax}
}

@misc{google-natural-language-entity,
	title = {{Method: documents.analyzeEntities {$\vert$} Cloud Natural Language API}},
	journal = {Google Cloud},
	year = {2019},
	month = {Dec},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeEntities}
}

@misc{einstein-language,
	title = {{Introduction to Salesforce Einstein Language}},
	journal = {Einstein Platform Services},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://metamind.readme.io/docs/intro-to-einstein-language}
}

@misc{einstein-language-sentiment,
	title = {{Community Sentiment Model}},
	journal = {Einstein Platform Services},
	year = {2021},
	month = {Nov},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://metamind.readme.io/docs/use-pre-built-models-sentiment}
}

@misc{ibm-natural-language,
	title = {{IBM Watson Natural Language Understanding - Overview}},
	year = {2021},
	month = {Aug},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://www.ibm.com/cloud/watson-natural-language-understanding}
}

@misc{ibm-natural-language-sentiment,
	title = {{Natural Language Understanding - IBM Cloud API Docs}},
	year = {2016},
	month = {May},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.ibm.com/apidocs/natural-language-understanding#sentiment}
}

@misc{ibm-natural-language-keyphrase,
	title = {{Natural Language Understanding - IBM Cloud API Docs}},
	year = {2016},
	month = {May},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.ibm.com/apidocs/natural-language-understanding#keywords}
}

@misc{ibm-natural-language-syntax,
	title = {{Natural Language Understanding - IBM Cloud API Docs}},
	year = {2016},
	month = {May},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.ibm.com/apidocs/natural-language-understanding#syntax}
}

@misc{ibm-natural-language-entity,
	title = {{Natural Language Understanding - IBM Cloud API Docs}},
	year = {2016},
	month = {May},
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.ibm.com/apidocs/natural-language-understanding#entities}
}


# References
[^aws-comprehend]: https://aws.amazon.com/comprehend/
[^aws-comprehend-sentiment]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectSentiment.html
[^aws-comprehend-keyphrase]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectKeyPhrases.html
[^aws-comprehend-syntax]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectSyntax.html
[^aws-comprehend-entity]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectEntities.html
[^aws-comprehend-language]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectDominantLanguage.html
[^aws-comprehend-pii]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectPiiEntities.html
[^azure-language]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/
[^azure-language-sentiment]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/sentiment-opinion-mining/quickstart?pivots=rest-api
[^azure-language-keyphrase]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/key-phrase-extraction/quickstart?pivots=rest-api
[^azure-language-entity]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/named-entity-recognition/quickstart?pivots=rest-api
[^azure-language-language]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/language-detection/quickstart
[^azure-language-pii]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/personally-identifiable-information/quickstart?pivots=rest-api
[^google-natural-language]: https://cloud.google.com/natural-language
[^google-natural-language-sentiment]: https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSentiment
[^google-natural-language-syntax]: https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSyntax
[^google-natural-language-entity]: https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeEntities
[^einstein-language]: https://metamind.readme.io/docs/intro-to-einstein-language
[^einstein-language-sentiment]: https://metamind.readme.io/docs/use-pre-built-models-sentiment
[^ibm-natural-language]: https://www.ibm.com/cloud/watson-natural-language-understanding
[^ibm-natural-language-sentiment]: https://cloud.ibm.com/apidocs/natural-language-understanding#sentiment
[^ibm-natural-language-keyphrase]: https://cloud.ibm.com/apidocs/natural-language-understanding#keywords
[^ibm-natural-language-syntax]: https://cloud.ibm.com/apidocs/natural-language-understanding#syntax
[^ibm-natural-language-entity]: https://cloud.ibm.com/apidocs/natural-language-understanding#entities

