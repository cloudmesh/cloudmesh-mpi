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
| Sentiment detection  | DetectSentiment [^ref2] | sentiment [^ref9]  | analyzeSentiment [^ref15] | CommunitySentiment [^ref19]  | Sentiment [^ref20]  |
|  Keyphrase extraction | DetectKeyPhrases [^ref3]  | keyPhrases [^ref10]  | ---  | ---  | Keywords [^ref22] |
|  Syntax detection | DetectSyntax [^ref4]  | --- | analyzeSyntax [^ref16]  | ---  | Syntax [^ref23]  |
|  Entity recognition | DetectEntities [^ref5]  |  entities/recognition/general [^ref11] | analyzeEntities [^ref17] | ---  | Entities [^ref24]  |
|  Language detection | DetectDominantLanguage [^ref6]  | languages [^ref12]  | (included in others)  |  --- | (included in others)  |
|  PII detection | DetectPiiEntities [^ref7]  | entities/recognition/pii [^ref13]  | ---  | ---  | ---  |

## Amazon Comprehend [^ref1]

Supported Interfaces:
AWS CLI, Python, Java

### Functions

The following is a non-exhaustive selection of functions provided by the API 

DetectSentiment [^ref2]
- language, text -> Sentiment [POSITIVE | NEGATIVE | NEUTRAL | MIXED], SentimentScore [float 0.0-1.0 for each possible sentiment]

DetectKeyPhrases [^ref3]
- language, text -> list of key phrases with confidence score and location in text

DetectSyntax [^ref4]
- language, text -> list of tokenized elements of the input text, each with a declared part of speech

DetectEntities [^ref5]
- custom endpoint model (optional), language, text -> list of detected entities with type, score, and location

DetectDominantLanguage [^ref6]
- text -> language code, score

DetectPiiEntities [^ref7]
- language, text -> list of entities with type, score

## Azure Cognitive Science for Language [^ref8]

Supported Interfaces:
REST API, Python, C#, Java, Javascript

### Functions

sentiment [^ref9]
- document, key, endpoint -> sentiment scores [positive, negative, neutral] for entire input as well as each sentence 

keyPhrases [^ref10]
- document, key, endpoint -> list of keyphrases, warnings, errors

entities/recognition/general [^ref11]
- document, key, endpoint -> list of recognized entities with their category, subcategory, and score

languages [^ref12]
- document, key, endpoint -> language name, code, and score

entities/recognition/pii [^ref13]
- document, key, endpoint -> detected PII with type, location, and score

## Google Natural Language API [^ref14]

Supported Interfaces:
REST API, Python, C#, JAVA, Go, Node.js, PHP, Ruby

### Functions

analyzeSentiment [^ref15]
- document, encodingType -> Sentiment object, language, sentences list (each with their own sentiment)

analyzeSyntax [^ref16]
- document, encodingType -> sentences list, tokens list, language

analyzeEntities [^ref17]
- docuent, encodingType -> entities list, language

## Salesforce Einstein Language [^ref18]

Supported Interfaces:
REST API

### Functions

CommunitySentiment [^ref19]
- document, auth token, cache control, model -> label [positive, negative, neutral], probability scores

## IBM Watson Natural Language Understanding [^ref21]

Supported Interfaces:
Rest API, Python, Java, Node, Go, .NET, Ruby, Swift, Unity

### Functions

Sentiment [^ref20]
- text/url, target keywords -> label, score for document & any target keywords

Keywords [^ref22]
- text/url, max # keywords, sentiment/emotion flags -> list of keywords, each with detected sentiment and emotion if flagged

Syntax [^ref23]
- text/url, sentences flag, optional tokens -> detected part of speech, location, and additonal tokens for each word + sentence (if flagged)

Entities [^ref24]
- text/url, max # entities, sentiment/emotion/mentions flags -> list of entities with detected labels & additional optional flags



# References
[^ref1]: https://aws.amazon.com/comprehend/
[^ref2]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectSentiment.html
[^ref3]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectKeyPhrases.html
[^ref4]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectSyntax.html
[^ref5]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectEntities.html
[^ref6]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectDominantLanguage.html
[^ref7]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectPiiEntities.html
[^ref8]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/
[^ref9]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/sentiment-opinion-mining/quickstart?pivots=rest-api
[^ref10]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/key-phrase-extraction/quickstart?pivots=rest-api
[^ref11]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/named-entity-recognition/quickstart?pivots=rest-api
[^ref12]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/language-detection/quickstart
[^ref13]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/personally-identifiable-information/quickstart?pivots=rest-api
[^ref14]: https://cloud.google.com/natural-language
[^ref15]: https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSentiment
[^ref16]: https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSyntax
[^ref17]: https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeEntities
[^ref18]: https://metamind.readme.io/docs/intro-to-einstein-language
[^ref19]: https://metamind.readme.io/docs/use-pre-built-models-sentiment
[^ref20]: https://cloud.ibm.com/apidocs/natural-language-understanding#sentiment
[^ref21]: https://www.ibm.com/cloud/watson-natural-language-understanding
[^ref22]: https://cloud.ibm.com/apidocs/natural-language-understanding#keywords
[^ref23]: https://cloud.ibm.com/apidocs/natural-language-understanding#syntax
[^ref24]: https://cloud.ibm.com/apidocs/natural-language-understanding#entities
