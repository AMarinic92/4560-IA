# COMP 4560 Project - Internet Archive

## AI-Powered Accessibility Checker

Our AI-powered Accessibility Checker is aimed at streamlining the process of ensuring digital content is accessible to all users. Leveraging advanced machine learning algorithms, our platform efficiently scans websites to detect potential accessibility issues. Our Accessibility Checker offers thorough analysis and practical recommendations for improvement. By providing developers, designers, and content creators with valuable insights, our solution contributes to creating a more inclusive digital environment where everyone can access and engage with content effortlessly. 

## Goals

### Web Content Accessibility Guidelines

In order to tackle accessibility issues, we first need to be able to define what it means to be accessible. As suggested to us by Brenton from the Internet Archive, for this project, we have set that definition to mean being [Web Content Accessibility Guidelines (WCAG) 2.2 level AA][1] compliant. WCAG is very comprehensive, and checking for all issues to meet compliance would be very difficult in the limited time that we have. As such, we needed to narrow down the list to a few issues we would like to tackle, and hopefully, this is something that can be explored and expanded on in the future.

#### WCAG 2.2 Success Criterion 1.1.1 Non-text Content:

**Criterion 1.1.1** states: "All non-text content that is presented to the user has a text alternative that serves the equivalent purpose." It then lists some exceptions, including decoration, such as an image that is only there for decoration or visual formatting. 

We attempted to meet this criterion by first parsing a webpage, finding all the images, and checking to see if those pages have alt-text. We then have an AI algorithm that creates a caption for the images that are missing captions. We also found an AI model that would be able to tell whether the image is decorative or not. Unfortunately, due to time constraints, we were unable to incorporate it into the pipeline.  

As a proof of concept, our checker works well. There exist more models, that would be simple enough to incorporate into the pipeline as well. For example, there are AI models that can compare two sentences, with which you could compare an existing alt-text with an AI-generated one to see how well an existing one fits. You could also use other models to try to fulfill other WCAG criteria, such as using models to generate captions for videos, or describe audio, as suggested in [Success Criterion 1.2.1][2], [Success Criterion 1.2.2][3], and [Success Criterion 1.2.3][4].

### JIRA

The Internet Archive also provided us with some of their JIRA ticket issues and an accessibility report to help us create our accessibility checker. 

For example, one of the issues was links that just said "Click Here", which is bad practice as it may cause issues for users of assistive technologies. We investigated using summarization and tokenization for generating descriptive links to assist with this issue.

### Feedback From Internet Archive

Throughout the process, we worked closely with our Internet Archive partner who was able to provide some feedback and suggest some features. 

Suggestions made:

- Initially, the issue and suggestion were separate tabs.
    - Feedback from Brenton was to put them together and have the suggestion next to the corresponding issue.
- A loading indicator while the checker is processing.
- To add an info button to explain to the user what is being checked.

## Installation & Usage
Follow the install instructions in each of the following:
- [Frontend](frontend/README.md)
- [Backend](backend/socket/readMe.md)
- [Docker](backend/socket/cmds/README.md)
Then launch chrome and find the app in the side panel.

## Contributors

- Tehillah Kangamba
- Andrew Marinic
- Rozen Noureev

## License

[AGPLv3](https://choosealicense.com/licenses/agpl-3.0/)

## Resources

[1]: https://www.w3.org/TR/WCAG22/
[2]: https://www.w3.org/TR/WCAG22/#audio-only-and-video-only-prerecorded
[3]: https://www.w3.org/TR/WCAG22/#captions-prerecorded
[4]: https://www.w3.org/TR/WCAG22/#audio-description-or-media-alternative-prerecorded

### Machine Learning

#### Models used

- Image Captioning: [https://huggingface.co/Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large)
- Summarization: [https://huggingface.co/facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)
- Token Classification: [https://huggingface.co/Jean-Baptiste/camembert-ner](https://huggingface.co/Jean-Baptiste/camembert-ner)
