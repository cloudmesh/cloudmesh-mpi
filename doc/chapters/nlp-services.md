# Survey of different NLP services and their features

## Introduction

There exist a multitude of APIs available that offer natural langauge processing services with pre-packaged, trained functions. This document will act as a survey for a number of these different services, highlighting their features and similarities.

- Amazon Comprehend (available through AWS)
- Azure Cognitive Service for Language
- Google Natural Language API
- Salesforce Einstein Language
- IBM Watson Natural Language Understanding


## Overview

The following table shows the most common features that are shared among APIs and links to the specific corresponding functions in their documentation.

|   | Amazon Comprehend  | Azure  | Google  | Einstein Language  | IBM Watson  |
|---|---|---|---|---|---|
| Sentiment detection  | DetectSentiment [^www-aws-comprehend-sentiment] | sentiment [^www-azure-language-sentiment]  | analyzeSentiment [^www-google-natural-language-sentiment] | CommunitySentiment [^www-einstein-language-sentiment]  | Sentiment [^www-ibm-natural-language-sentiment]  |
|  Keyphrase extraction | DetectKeyPhrases [^www-aws-comprehend-keyphrase]  | keyPhrases [^www-azure-language-keyphrase]  | ---  | ---  | Keywords [^www-ibm-natural-language-keyphrase] |
|  Syntax detection | DetectSyntax [^www-aws-comprehend-syntax]  | --- | analyzeSyntax [^www-google-natural-language-syntax]  | ---  | Syntax [^www-ibm-natural-language-syntax]  |
|  Entity recognition | DetectEntities [^www-aws-comprehend-entity]  |  entities/recognition/general [^www-azure-language-entity] | analyzeEntities [^www-google-natural-language-entity] | ---  | Entities [^www-ibm-natural-language-entity]  |
|  Language detection | DetectDominantLanguage [^www-aws-comprehend-language]  | languages [^www-azure-language-language]  | (included in others)  |  --- | (included in others)  |
|  PII detection | DetectPiiEntities [^www-aws-comprehend-pii]  | entities/recognition/pii [^www-azure-language-pii]  | ---  | ---  | ---  |

## Amazon Comprehend [^www-aws-comprehend]

Comprehend is Amazon's solution for cloud-based NLP. It is available with an AWS account. To use, it requires use of either the AWS Command Line Interface or an AWS sdk for Python, Java, or .NET. Notable features include functionality for giving batches of documents to be processed as well as submission of multiple jobs in a list. The DetectEntities function also allows use of a custom-trained model, but many other functions do not.

Supported Interfaces:
AWS CLI, Python, Java, .NET

### Functions

The following is a non-exhaustive selection of pre-configured functions provided by the API that are common among NLP services.

DetectSentiment [^www-aws-comprehend-sentiment]
- language, text -> Sentiment [POSITIVE | NEGATIVE | NEUTRAL | MIXED], SentimentScore [float 0.0-1.0 for each possible sentiment]

DetectKeyPhrases [^www-aws-comprehend-keyphrase]
- language, text -> list of key phrases with confidence score and location in text

DetectSyntax [^www-aws-comprehend-syntax]
- language, text -> list of tokenized elements of the input text, each with a declared part of speech

DetectEntities [^www-aws-comprehend-entity]
- custom endpoint model (optional), language, text -> list of detected entities with type, score, and location

DetectDominantLanguage [^www-aws-comprehend-language]
- text -> language code, score

DetectPiiEntities [^www-aws-comprehend-pii]
- language, text -> list of entities with type, score

## Azure Cognitive Service for Language [^www-azure-language]

Azure Cognitive Service for Language is Microsoft's solution for cloud-based NLP. It requires an Azure account. Notable features include a variety of pre-configured, non-customizable models for different functions as well as the addition of some customizable options which allow the input of one's own custom-trained model.

Supported Interfaces:
REST API, Python, C#, Java, Javascript

### Functions

The following is a non-exhaustive selection of pre-configured functions provided by the API that are common among NLP services.

sentiment [^www-azure-language-sentiment]
- document, key, endpoint -> sentiment scores [positive, negative, neutral] for entire input as well as each sentence 

keyPhrases [^www-azure-language-keyphrase]
- document, key, endpoint -> list of keyphrases, warnings, errors

entities/recognition/general [^www-azure-language-entity]
- document, key, endpoint -> list of recognized entities with their category, subcategory, and score

languages [^www-azure-language-language]
- document, key, endpoint -> language name, code, and score

entities/recognition/pii [^www-azure-language-pii]
- document, key, endpoint -> detected PII with type, location, and score

## Google Natural Language API [^www-google-natural-language]

Google Natural Language API is Google's solution for cloud-based NLP. It requires a Google Cloud account. The Natural Language API includes only the pre-configured models for common NLP functions, though Google also offers services specific to healthcare NLP as well as a code-free ML model manager called AutoML as part of Google Cloud.

Supported Interfaces:
REST API, Python, C#, JAVA, Go, Node.js, PHP, Ruby

### Functions

The following is a non-exhaustive selection of pre-configured functions provided by the API that are common among NLP services.

analyzeSentiment [^www-google-natural-language-sentiment]
- document, encodingType -> Sentiment object, language, sentences list (each with their own sentiment)

analyzeSyntax [^www-google-natural-language-syntax]
- document, encodingType -> sentences list, tokens list, language

analyzeEntities [^www-google-natural-language-entity]
- docuent, encodingType -> entities list, language

## Salesforce Einstein Language [^www-einstein-language]

Einstein Language is Salesforce's solution to cloud-based NLP. It requires a Salesforce/Einstein account. It is under the umbrella of Einstein AI, which also includes Einstein Vision for image processing purposes. At the moment, Einstein Language only includes two main features, Intent and Sentiment. Intent analyzes meaning in text for the specific purpose of deciding market intent in customers. Sentiment is comparable to the classic sentiment detection provided by other NLP services, and therefore it is what will be covered in this document.

Supported Interfaces:
REST API

### Functions

The following is a non-exhaustive selection of pre-configured functions provided by the API that are common among NLP services.

CommunitySentiment [^www-einstein-language-sentiment]
- document, auth token, cache control, model -> label [positive, negative, neutral], probability scores

## IBM Watson Natural Language Understanding [^www-ibm-natural-language]

Watson Natural Language Understanding is IBM's solution to cloud-based NLP. It requires an IBM Cloud account. Notable features include the ability to use custom-trained models for each of its functions as well as access to related NLP services in the IBM Cloud platform such as Watson Knowledge Studio and Watson Discovery, which provide NLP functions and customized model training that tends to be more specific to businesses.

Supported Interfaces:
Rest API, Python, Java, Node, Go, .NET, Ruby, Swift, Unity

### Functions

The following is a non-exhaustive selection of pre-configured functions provided by the API that are common among NLP services.

Sentiment [^www-ibm-natural-language-sentiment]
- text/url, target keywords -> label, score for document & any target keywords

Keywords [^www-ibm-natural-language-keyphrase]
- text/url, max # keywords, sentiment/emotion flags -> list of keywords, each with detected sentiment and emotion if flagged

Syntax [^www-ibm-natural-language-syntax]
- text/url, sentences flag, optional tokens -> detected part of speech, location, and additonal tokens for each word + sentence (if flagged)

Entities [^www-ibm-natural-language-entity]
- text/url, max # entities, sentiment/emotion/mentions flags -> list of entities with detected labels & additional optional flags

# Bibtex

@misc{www-aws-comprehend,
	title = {{Natural Language Processing - Amazon Comprehend}},
	author = {{Amazon Web Services, Inc}},
	year = 2021,
	month = oct,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://aws.amazon.com/comprehend}
}

@misc{www-aws-comprehend-sentiment,
	title = {{DetectSentiment - Amazon Comprehend}},
	author = {{Amazon Web Services, Inc}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectSentiment.html}
}

@misc{www-aws-comprehend-keyphrase,
	title = {{DetectKeyPhrases - Amazon Comprehend}},
	author = {{Amazon Web Services, Inc}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectKeyPhrases.html}
}

@misc{www-aws-comprehend-syntax,
	title = {{DetectSyntax - Amazon Comprehend}},
	author = {{Amazon Web Services, Inc}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectSyntax.html}
}

@misc{www-aws-comprehend-entity,
	title = {{DetectEntities - Amazon Comprehend}},
	author = {{Amazon Web Services, Inc}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectEntities.html}
}

@misc{www-aws-comprehend-language,
	title = {{DetectDominantLanguage - Amazon Comprehend}},
	author = {{Amazon Web Services, Inc}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectDominantLanguage.html}
}

@misc{www-aws-comprehend-pii,
	title = {{DetectPiiEntities - Amazon Comprehend}},
	author = {{Amazon Web Services, Inc}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectPiiEntities.html}
}

@misc{www-azure-language,
	author = {{Microsoft}},
	title = {{Azure Cognitive Service for language documentation}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.microsoft.com/en-us/azure/cognitive-services/language-service}
}

@misc{www-azure-language-sentiment,
	author = {{Microsoft}},
	title = {{Quickstart: Use the Sentiment Analysis client library and REST API - Azure Cognitive Services}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/sentiment-opinion-mining/quickstart?pivots=rest-api}
}

@misc{www-azure-language-keyphrase,
	author = {{Microsoft}},
	title = {{Quickstart: Use the Key Phrase Extraction client library - Azure Cognitive Services}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/key-phrase-extraction/quickstart?pivots=rest-api}
}

@misc{www-azure-language-entity,
	author = {{Microsoft}},
	title = {{Quickstart: Use the NER client library - Azure Cognitive Services}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/named-entity-recognition/quickstart?pivots=rest-api}
}

@misc{www-azure-language-language,
	author = {{Microsoft}},
	title = {{Quickstart: Use the Language Detection client library - Azure Cognitive Services}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/language-detection/quickstart?pivots=rest-api}
}

@misc{www-azure-language-pii,
	author = {{Microsoft}},
	title = {{Quickstart: Detect Personally Identifying Information (PII) in text - Azure Cognitive Services}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/personally-identifiable-information/quickstart?pivots=rest-api}
}

@misc{www-google-natural-language,
	title = {{Cloud Natural Language - Google Cloud}},
	author = {{Google Cloud}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.google.com/natural-language}
}

@misc{www-google-natural-language-sentiment,
	title = {{Method: documents.analyzeSentiment - Cloud Natural Language API}},
	author = {{Google Cloud}},
	year = 2019,
	month = dec,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSentiment}
}

@misc{www-google-natural-language-syntax,
	title = {{Method: documents.analyzeSyntax - Cloud Natural Language API}},
	author = {{Google Cloud}},
	year = 2019,
	month = dec,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSyntax}
}

@misc{www-google-natural-language-entity,
	title = {{Method: documents.analyzeEntities - Cloud Natural Language API}},
	author = {{Google Cloud}},
	year = 2019,
	month = dec,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeEntities}
}

@misc{www-einstein-language,
	title = {{Introduction to Salesforce Einstein Language}},
	author = {{Einstein Platform Services}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://metamind.readme.io/docs/intro-to-einstein-language}
}

@misc{www-einstein-language-sentiment,
	title = {{Community Sentiment Model}},
	author = {{Einstein Platform Services}},
	year = 2021,
	month = nov,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://metamind.readme.io/docs/use-pre-built-models-sentiment}
}

@misc{www-ibm-natural-language,
	title = {{IBM Watson Natural Language Understanding - Overview}},
	author = {{IBM}},
	year = 2021,
	month = aug,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://www.ibm.com/cloud/watson-natural-language-understanding}
}

@misc{www-ibm-natural-language-sentiment,
	title = {{Natural Language Understanding - IBM Cloud API Docs}},
	author = {{IBM}},
	year = 2016,
	month = may,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.ibm.com/apidocs/natural-language-understanding#sentiment}
}

@misc{www-ibm-natural-language-keyphrase,
	title = {{Natural Language Understanding - IBM Cloud API Docs}},
	year = 2016,
	month = may,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.ibm.com/apidocs/natural-language-understanding#keywords}
}

@misc{www-ibm-natural-language-syntax,
	title = {{Natural Language Understanding - IBM Cloud API Docs}},
	year = 2016,
	month = may,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.ibm.com/apidocs/natural-language-understanding#syntax}
}

@misc{www-ibm-natural-language-entity,
	title = {{Natural Language Understanding - IBM Cloud API Docs}},
	year = 2016,
	month = may,
	note = {[Online; accessed 9. Nov. 2021]},
	url = {https://cloud.ibm.com/apidocs/natural-language-understanding#entities}
}


# References
[^www-aws-comprehend]: https://aws.amazon.com/comprehend/
[^www-aws-comprehend-sentiment]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectSentiment.html
[^www-aws-comprehend-keyphrase]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectKeyPhrases.html
[^www-aws-comprehend-syntax]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectSyntax.html
[^www-aws-comprehend-entity]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectEntities.html
[^www-aws-comprehend-language]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectDominantLanguage.html
[^www-aws-comprehend-pii]: https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectPiiEntities.html
[^www-azure-language]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/
[^www-azure-language-sentiment]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/sentiment-opinion-mining/quickstart?pivots=rest-api
[^www-azure-language-keyphrase]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/key-phrase-extraction/quickstart?pivots=rest-api
[^www-azure-language-entity]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/named-entity-recognition/quickstart?pivots=rest-api
[^www-azure-language-language]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/language-detection/quickstart
[^www-azure-language-pii]: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/personally-identifiable-information/quickstart?pivots=rest-api
[^www-google-natural-language]: https://cloud.google.com/natural-language
[^www-google-natural-language-sentiment]: https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSentiment
[^www-google-natural-language-syntax]: https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSyntax
[^www-google-natural-language-entity]: https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeEntities
[^www-einstein-language]: https://metamind.readme.io/docs/intro-to-einstein-language
[^www-einstein-language-sentiment]: https://metamind.readme.io/docs/use-pre-built-models-sentiment
[^www-ibm-natural-language]: https://www.ibm.com/cloud/watson-natural-language-understanding
[^www-ibm-natural-language-sentiment]: https://cloud.ibm.com/apidocs/natural-language-understanding#sentiment
[^www-ibm-natural-language-keyphrase]: https://cloud.ibm.com/apidocs/natural-language-understanding#keywords
[^www-ibm-natural-language-syntax]: https://cloud.ibm.com/apidocs/natural-language-understanding#syntax
[^www-ibm-natural-language-entity]: https://cloud.ibm.com/apidocs/natural-language-understanding#entities

