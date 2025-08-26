
- **[3180-sqlite-ai-agent.json](workflows/3180-sqlite-ai-agent.json)**
  - **Description:** This flow allows interacting with an SQLite database using an artificial intelligence agent. It downloads, extracts and loads the database locally, then uses the SQL agent to answer questions based on the data.
  - **Complexity:** Low (1 nodes)

- **[3189-ubicacion-trabajo.json](workflows/3189-ubicacion-trabajo.json)**
  - **Description:** This automatic flow automatically records entry and exit times based on location using Webhooks, Google Sheets and Drive. It detects if the worksheet exists, creates a new one if not present and records time data with date and address.
  - **Complexity:** Low (1 nodes)

- **[3240-strava-to-sheets.json](workflows/3240-strava-to-sheets.json)**
  - **Description:** This flow schedules a task that every two hours extracts Strava activities, filters those not saved in Google Sheets and processes them to update a spreadsheet with details such as distance, date, time and elevation gain.
  - **Complexity:** Low (1 nodes)

- **[3259-notion-md-sincro.json](workflows/3259-notion-md-sincro.json)**
  - **Description:** This flow automates the synchronization of Notion blocks by converting rich text to Markdown format and vice versa, allowing content to be updated with formatting.
  - **Complexity:** Low (1 nodes)

- **[3268-prompt-generator.json](workflows/3268-prompt-generator.json)**
  - **Description:** Flow to generate and organize optimized prompts in Airtable using Google Gemini. It allows categorizing and structuring chatbot prompts for better handling in n8n.
  - **Complexity:** Low (1 nodes)

- **[3296-shopify-to-google-spreadsheet.json](workflows/3296-shopify-to-google-spreadsheet.json)**
  - **Description:** This flow extracts customer information from Shopify and exports it to a Google Sheets spreadsheet. It uses a loop to retrieve paginated data until there are no more pages, processing the information and continuously updating.
  - **Complexity:** Low (1 nodes)

- **[3302-webpage-change-monitor.json](workflows/3302-webpage-change-monitor.json)**
  - **Description:** Automated flow to detect changes on a web page and notify via email when there is a modification. It uses a content hash for comparison and records activities in Google Sheets.
  - **Complexity:** Low (1 nodes)

- **[3333-Enrich_Company_Data.json](workflows/3333-Enrich_Company_Data.json)**
  - **Description:** This flow automates the enrichment of business data using Google Sheets, OpenAI and a web extraction tool. It retrieves information from a spreadsheet, uses an artificial intelligence agent to analyze websites via ScrapingBee and updates the data in real time.
  - **Complexity:** Low (1 nodes)

- **[0531-webflow-form-trigger.json](workflows/0531-webflow-form-trigger.json)**
  - **Description:** This automatic flow is activated when a form is submitted on a Webflow web page and collects the data for processing.
  - **Complexity:** Low (1 nodes)

- **[0599-box-folder-file-events.json](workflows/0599-box-folder-file-events.json)**
  - **Description:** This automatic flow is activated when files or folders are moved or downloaded in a specific Box folder.
  - **Complexity:** Low (1 nodes)

- **[0054-clickup-trigger.json](workflows/0054-clickup-trigger.json)**
  - **Description:** This automatic flow is activated upon receiving updates of any event in the ClickUp tool.
  - **Complexity:** Low (1 nodes)

- **[0542-asana-tweet-event-trigger.json](workflows/0542-asana-tweet-event-trigger.json)**
  - **Description:** This automatic flow allows receiving updates when an event occurs in Asana related to tweets.
  - **Complexity:** Low (1 nodes)

- **[0567-github-monitor-repo.json](workflows/0567-github-monitor-repo.json)**
  - **Description:** This flow monitors any activity in the GitHub repository 'n8n-io/n827-docs' via a webhook, using predefined credentials for the API.
  - **Complexity:** Low (1 nodes)

- **[0568-gitlab-trigger-n8n-docs.json](workflows/0568-gitlab-trigger-n8n-docs.json)**
  - **Description:** This flow monitors events in the GitLab repository n8n-io/n8n-docs via a webhook.
  - **Complexity:** Low (1 nodes)

- **[0569-bitbucket-push-monitor.json](workflows/0569-bitbucket-push-monitor.json)**
  - **Description:** This flow is automatically activated when there is a push event in the 'test' Bitbucket repository.
  - **Complexity:** Low (1 nodes)

- **[0603-jira-trigger-any-event.json](workflows/0603-jira-trigger-any-event.json)**
  - **Description:** This flow monitors any event in Jira Software Cloud via a web connection.
  - **Complexity:** Low (1 nodes)

- **[0640-helpscout-customer-created.json](workflows/0640-helpscout-customer-created.json)**
  - **Description:** This flow specifically listens for the 'customer.created' event in HelpScout using an OAuth webhook.
  - **Complexity:** Low (1 nodes)

- **[0667-taiga-event-trigger.json](workflows/0667-taiga-event-trigger.json)**
  - **Description:** This flow listens for events in the specific Taiga project via a webhook trigger.
  - **Complexity:** Low (1 nodes)

- **[1176-zendesk-ticket-updates.json](workflows/1176-zendesk-ticket-updates.json)**
  - **Description:** This automatic flow is configured to receive ticket updates in Zendesk via a webhook, although it is not active.
  - **Complexity:** Low (1 nodes)

- **[1251-trello-list-updates.json](workflows/1251-trello-list-updates.json)**
  - **Description:** This flow monitors and receives updates on changes in a specific Trello list.
  - **Complexity:** Low (1 nodes)
### Content Management and Social Networks

- **[0007-social-media-creator.json](workflows/0007-social-media-creator.json)**
  - **Description:** This automatic flow allows a chatbot to create optimized content for multiple social networks (X-Twitter, Instagram, Facebook, LinkedIn, Threads, YouTube Shorts) using LLM models and web search tools. It generates posts with specific JSON structures and creates images using external services such as pollinations.ai.
  - **Complexity:** High (100 nodes)

- **[2912-youtube-ai-summarizer.json](workflows/2912-youtube-ai-summarizer.json)**
  - **Description:** This flow automates the summarization and analysis of YouTube playlists or videos using AI. It detects URLs, processes transcripts, generates structured summaries and stores embeddings for contextualized responses.
  - **Complexity:** High (72 nodes)

- **[1409-automated_social_media_factory.json](workflows/1409-automated_social_media_factory.json)**
  - **Description:** Generates content for social networks automatically.
  - **Complexity:** High (56 nodes)

- **[1279-spotify_to_youtube_sync.json](workflows/1279-spotify_to_youtube_sync.json)**
  - **Description:** Synchronizes Spotify lists with YouTube.
  - **Complexity:** High (54 nodes)

- **[3044-video_generator_short_form.json](workflows/3044-video_generator_short_form.json)**
  - **Description:** This flow automatically generates short videos with AI, using OpenAI to generate prompts, Flux and Kling from PiAPI to create images and videos, ElevenLabs for voice and Creatomate to render the final video. Then it uploads them to all social networks.
  - **Complexity:** High (51 nodes)

- **[2985-hacker_news_video_content.json](workflows/2985-hacker_news_video_content.json)**
  - **Description:** This flow automates the conversion of Hacker News articles to video content using RunwayML and LeonardoAI to generate personalized images and videos.
  - **Complexity:** High (48 nodes)

- **[2965-instagram-content-generator.json](workflows/2965-instagram-content-generator.json)**
  - **Description:** This flow automates the creation of Instagram content using current trends and AI image generation. It downloads popular Instagram content via an API, analyzes images with GPT-4, creates attractive captions and generates new images with Flux AI. It publishes the content to your business Instagram account and monitors the status of publications.
  - **Complexity:** High (44 nodes)

- **[2964-image_generator_9_16.json](workflows/2964-image_generator_9_16.json)**
  - **Description:** This flow generates 9:16 aspect ratio images from content and brand guides using OpenAI and Leonardo.ai to create optimized visual assets.
  - **Complexity:** High (39 nodes)

- **[1416-video-social-generator.json](workflows/1416-video-social-generator.json)**
  - **Description:** Generates short videos for social networks.
  - **Complexity:** High (38 nodes)

- **[2952-crawler-ai-scraper.json](workflows/2952-crawler-ai-scraper.json)**
  - **Description:** Flow that uses AI agents to autonomously extract social media links from websites.
  - **Complexity:** High (38 nodes)

- **[2576-AI-WordPress-Article-Creator.json](workflows/2576-AI-WordPress-Article-Creator.json)**
  - **Description:** This automatic flow uses artificial intelligence to generate SEO articles in WordPress based on keywords provided by the user. It includes creating titles, subtitles, chapters and verification with Wikipedia.
  - **Complexity:** High (37 nodes)

- **[2930-exam-question-generator.json](workflows/2930-exam-question-generator.json)**
  - **Description:** Flow to generate both open and closed exam questions from content in Google Docs using Qdrant vectors and different language models.
  - **Complexity:** High (37 nodes)

- **[2942-categorizador-ai-outlook.json](workflows/2942-categorizador-ai-outlook.json)**
  - **Description:** This flow automatically categorizes Outlook emails using AI to classify them into different folders based on their content.
  - **Complexity:** High (36 nodes)

- **[1148-linkedin-automation.json](workflows/1148-linkedin-automation.json)**
  - **Description:** This automated flow seeks to obtain recent articles about LinkedIn through scheduled searches, extract their links and then generate contributions using AI technology.
  - **Complexity:** High (33 nodes)

- **[2568-service-page-seo-blueprint.json](workflows/2568-service-page-seo-blueprint.json)**
  - **Description:** This flow analyzes the SEO performance of service pages, comparing structures and content with competitors in real time to create optimized strategies.
  - **Complexity:** High (33 nodes)

- **[2572-youtube-automation-generative.json](workflows/2572-youtube-automation-generative.json)**
  - **Description:** This automatic flow allows obtaining YouTube videos and generating titles, descriptions and SEO information to automate the necessary functions.
  - **Complexity:** High (33 nodes)

- **[3048-analyze_youtube_workflow.json](workflows/3048-analyze_youtube_workflow.json)**
  - **Description:** This flow analyzes YouTube videos to summarize them, generate transcripts and extract content using Google's Gemini AI API. It allows different types of analysis such as concise summaries, verbatim transcripts, subtitles with timestamps and more.
  - **Complexity:** High (33 nodes)

- **[0818-ai-summary-wordpress.json](workflows/0818-ai-summary-wordpress.json)**
  - **Description:** This automatic flow analyzes and classifies WordPress content to determine if it already includes an AI-generated summary, generating new summaries with GPT-4o-mini when necessary.
  - **Complexity:** High (32 nodes)

- **[3170-auto-tag-wordpress.json](workflows/3170-auto-tag-wordpress.json)**
  - **Description:** This flow automates the assignment of tags in WordPress using AI. It analyzes RSS entries, generates and structures tags, creates new ones if necessary and updates existing ones.
  - **Complexity:** High (32 nodes)

- **[2972-youtube-ai-agent.json](workflows/2972-youtube-ai-agent.json)**
  - **Description:** This flow automates the extraction of details and transcripts from YouTube videos, which are processed by an artificial intelligence agent to allow contextualized conversation and detailed content analysis.
  - **Complexity:** High (29 nodes)

- **[1008-workflow-pdf-wordpress-ai.json](workflows/1008-workflow-pdf-wordpress-ai.json)**
  - **Description:** This automatic flow transforms PDF documents into blog entries formatted for WordPress, using AI to generate content and titles, creating images with pollinations.ai and incorporating human review via Gmail.
  - **Complexity:** High (27 nodes)

- **[2945-automate-blog-ai.json](workflows/2945-automate-blog-ai.json)**
  - **Description:** This flow automates the creation of blog articles in brand voice using AI. It analyzes existing content to extract style and tone characteristics, then generates new articles consistent with them.
  - **Complexity:** High (27 nodes)

- **[3229-ai_content_generator.json](workflows/3229-ai_content_generator.json)**
  - **Description:** This flow uses AI to analyze articles existing and extract voice and style characteristics, then generates new content following those guidelines and publishes to WordPress.
  - **Complexity:** High (27 nodes)

- **[2584-youtube-video-analysis.json](workflows/2584-youtube-video-analysis.json)**
  - **Description:** This flow analyzes YouTube videos to generate summaries, transcripts and detailed scene descriptions. It allows choosing the type of analysis via the 'promptType' variable (transcript, summary, scene) and incorporates a Gemini model for processing.
  - **Complexity:** High (26 nodes)

- **[0929-analisis_comentarios_youtube.json](workflows/0929-analisis_comentarios_youtube.json)**
  - **Description:** This flow analyzes YouTube video comments using the Google API and GPT-4o-mini to generate a detailed report with insights into audience trends, featured topics and practical recommendations.
  - **Complexity:** High (25 nodes)

- **[1010-workflow-contact-form-automation.json](workflows/1010-workflow-contact-form-automation.json)**
  - **Description:** This automatic flow classifies WordPress (CF7) form responses and generates personalized email drafts to efficiently respond to customers.
  - **Complexity:** High (24 nodes)

- **[0906-gmail-reply-drafts-openai-assistant.json](workflows/0906-gmail-reply-drafts-openai-assistant.json)**
  - **Description:** This automatic flow allows Gmail to respond to messages with the help of OpenAI Assistant, creating response drafts based on email content and removing tags that trigger this action after composing the message.
  - **Complexity:** High (23 nodes)

- **[2578-analisis-contenido-brand.json](workflows/2578-analisis-contenido-brand.json)**
  - **Description:** This automatic flow allows a user to configure a URL to extract markdown content, clean it leaving only text, generate a concise summary and analyze its sentiment with Google Gemini models.
  - **Complexity:** High (23 nodes)

- **[2582-auto-article-generation.json](workflows/2582-auto-article-generation.json)**
  - **Description:** This automatic flow uses the Perplexity model to generate initial content and then refines it through iterations using OpenAI generative models, finally publishing it to a platform like Contentful.
  - **Complexity:** High (23 nodes)

- **[2739-email-ai-reply.json](workflows/2739-email-ai-reply.json)**
  - **Description:** This automatic flow processes emails with specific tags by transferring their content to the OpenAI Assistant to generate a response draft. The workflow includes everything from email extraction to final sending and subsequent removal of trigger tags.
  - **Complexity:** High (23 nodes)

- **[3266-yt-ai-playlist.json](workflows/3266-yt-ai-playlist.json)**
  - **Description:** This flow creates and updates a YouTube playlist with AI news, deleting the previous one and notifying its creation.
  - **Complexity:** High (23 nodes)

- **[2593-seo-blog-generator-flujo-automatico.json](workflows/2593-seo-blog-generator-flujo-automatico.json)**
  - **Description:** This automatic flow allows a user to submit a research query related to male health topics to be processed by multiple AI nodes, generating structured content such as titles, subtitles and hashtags based on the information provided. It then uses this structure along with research collected via Perplexity.ai to create a complete blog article.
  - **Complexity:** High (22 nodes)

- **[2847-paulgraham-essays-milvus.json](workflows/2847-paulgraham-essays-milvus.json)**
  - **Description:** This flow extracts the titles of Paul Graham's essays, obtains their content, processes them and stores them in Milvus to then answer questions about them.
  - **Complexity:** High (22 nodes)

- **[2798-podcast-summarizer.json](workflows/2798-podcast-summarizer.json)**
  - **Description:** This flow automates the creation of a daily summary of specific podcasts by genre. It uses the Taddy API to get the most popular podcast lists, downloads selected episodes, transcribes their content with Whisper and then generates a summary using OpenAI. The result is sent via email.
  - **Complexity:** High (21 nodes)

- **[2960-video_analyzer_youtube.json](workflows/2960-video_analyzer_youtube.json)**
  - **Description:** This flow uses different language models to analyze a YouTube video through its transcript, structuring the analysis in JSON format and sending the results by email.
  - **Complexity:** High (21 nodes)

- **[3061-wordpress-ai-optimizer.json](workflows/3061-wordpress-ai-optimizer.json)**
  - **Description:** This flow automates the creation and optimization of WordPress entries using AI to generate SEO-friendly titles, articles and meta tags, as well as handling images and updating spreadsheets.
  - **Complexity:** High (21 nodes)

- **[0796-n8n-reAct-scraper.json](workflows/0796-n8n-reAct-scraper.json)**
  - **Description:** This flow uses a ReAct AI agent with the HTTP_Request_Tool to extract and process HTML content via HTTP requests, applying page length limitations and simplifying it according to parameters.
  - **Complexity:** High (20 nodes)

- **[1239-wordpress-multi-social-publisher.json](workflows/1239-wordpress-multi-social-publisher.json)**
  - **Description:** This automated flow allows publishing WordPress content to multiple social networks using language models and structured processing.
  - **Complexity:** High (20 nodes)

- **[2692-http-web-content-processor.json](workflows/2692-http-web-content-processor.json)**
  - **Description:** This flow processes an HTTP request to obtain content from a web page, converts it to Markdown and applies limitations such as removing links and images if the method is simplified. It handles errors and formats the output according to the provided parameters.
  - **Complexity:** High (20 nodes)

- **[2743-youtube-rss-generator.json](workflows/2743-youtube-rss-generator.json)**
  - **Description:** This flow generates custom RSS URLs for YouTube channels and specific videos in different formats (ATOM, JSON, MRSS, PLAINTEXT, SFEED and XML) using external sources.
  - **Complexity:** High (20 nodes)

- **[2863-youtube-mcp-server.json](workflows/2863-youtube-mcp-server.json)**
  - **Description:** This flow configures an MCP server that uses external tools to perform YouTube searches, download transcripts and monitor usage metrics with APIFY.com.
  - **Complexity:** High (20 nodes)

- **[2738-gmail-label-assigner.json](workflows/2738-gmail-label-assigner.json)**
  - **Description:** This flow automates the assignment of labels to new Gmail messages using AI. It analyzes emails and determines which labels to apply based on their content.
  - **Complexity:** High (19 nodes)

- **[3083-linkedin-profile-finder.json](workflows/3083-linkedin-profile-finder.json)**
  - **Description:** This flow automates the search for LinkedIn profiles through a form where the user provides the full name and company. It uses Bright Data to perform Google searches and GPT-4o-mini to analyze the results, extract relevant information and generate a personalized email follow-up.
  - **Complexity:** High (19 nodes)

- **[0026-linkedin-top-sourcer.json](workflows/0026-linkedin-top-sourcer.json)**
  - **Description:** This flow allows finding LinkedIn profiles using boolean search techniques from a natural description of the candidate.
  - **Complexity:** High (18 nodes)

- **[1134-youtube-moments-analyzer.json](workflows/1134-youtube-moments-analyzer.json)**
  - **Description:** This flow analyzes YouTube videos for engaging moments where intensity exceeds a threshold and are not too close to each other, generating a structured response with the most relevant temporal coordinates.
  - **Complexity:** High (18 nodes)

- **[0910-url-markdown-batch.json](workflows/0910-url-markdown-batch.json)**
  - **Description:** This flow processes URLs in batches of 10, uses the Firecrawl API to convert HTML content to markdown and extract links, managing provider limitations.
  - **Complexity:** High (17 nodes)

- **[1144-firecrawl-markdown-scraper.json](workflows/1144-firecrawl-markdown-scraper.json)**
  - **Description:** This flow automates the extraction of web content in Markdown format and its links using the Firecrawl API.
  - **Complexity:** High (17 nodes)

- **[1146-digitalocean-snapshots-management.json](workflows/1146-digitalocean-snapshots-management.json)**
  - **Description:** This automatic flow automatically manages DigitalOcean instance snapshots, keeping a maximum of 4 and deleting the oldest ones.
  - **Complexity:** High (17 nodes)

- **[1413-automate_blog_creation.json](workflows/1413-automate_blog_creation.json)**
  - **Description:** Automates the creation of blog posts.
  - **Complexity:** High (17 nodes)

- **[2622-auto-content-wordpress.json](workflows/2622-auto-content-wordpress.json)**
  - **Description:** This automatic flow allows generating complete HTML content with SEO-optimized titles and specific keywords, as well as incorporating a Pexels image every time an article is published in WordPress.
  - **Complexity:** High (17 nodes)

- **[3136-tavily-search-extract.json](workflows/3136-tavily-search-extract.json)**
  - **Description:** This flow automates the search and extraction of information using the Tavily API, filtering results by relevance and summarizing content with OpenAI.
  - **Complexity:** High (17 nodes)

- **[1497-speed-up-social-media-banners-with-bannerbearcom.json](workflows/1497-speed-up-social-media-banners-with-bannerbearcom.json)**
  - **Description:** This flow allows content generation using OpenAI/GPT, Webhook, Twitter/X with artificial intelligence through webhooks and APIs.
  - **Complexity:** High (16 nodes)

- **[0776-youtube-seo-blog-generator.json](workflows/0776-youtube-seo-blog-generator.json)**
  - **Description:** This automatic flow allows extracting the transcript of YouTube videos using Dumpling AI, generating a complete SEO blog article with OpenAI GPT-4o based on that transcript and sending it as an email along with a generated image.
  - **Complexity:** Medium (15 nodes)

- **[0884-auto-post-sociales-n8n.json](workflows/0884-auto-post-sociales-n8n.json)**
  - **Description:** This automatic flow, triggered daily at 10:00 PM via a scheduled trigger, collects information from a Google spreadsheet (URL and video description) and integrates with the Blotato API to publish the content on multiple social platforms without manual intervention.
  - **Complexity:** Medium (15 nodes)

- **[0852-strapi-testimonials-automation.json](workflows/0852-strapi-testimonials-automation.json)**
  - **Description:** This automated flow seeks to collect and analyze positive testimonials in a Strapi system through integration with Twitter.
  - **Complexity:** Medium (14 nodes)

- **[2544-n8n-chatbot-car-offer.json](workflows/2544-n8n-chatbot-car-offer.json)**
  - **Description:** This automatic flow allows a LINE chatbot to interact with the sell.peddle.com website to get an offer for a used car. It logs into Airtop, loads the site and simulates interactions such as clicking or typing text when instructed by analyzing the current screen content.
  - **Complexity:** Medium (14 nodes)

- **[2837-linkedin-posts-generator.json](workflows/2837-linkedin-posts-generator.json)**
  - **Description:** This flow automates the generation of promotional LinkedIn messages for each blog post extracted from Ghost. It uses an AI agent to create engaging content and records it in a Google spreadsheet.
  - **Complexity:** Medium (14 nodes)

- **[2971-youtube-automatic-metadata-uploader.json](workflows/2971-youtube-automatic-metadata-uploader.json)**
  - **Description:** Flow to upload videos to YouTube with automatically optimized metadata using transcripts and AI.
  - **Complexity:** Medium (14 nodes)

- **[3022-youtube_transcriber.json](workflows/3022-youtube_transcriber.json)**
  - **Description:** This flow transcribes YouTube videos by validating the URL and structuring the text with OpenAI for a clean output in Portuguese.
  - **Complexity:** Medium (14 nodes)

- **[3142-social-media-publisher.json](workflows/3142-social-media-publisher.json)**
  - **Description:** This automatic flow manages content publishing on social networks such as Instagram, LinkedIn, Facebook, X and TikTok through a form that accepts photos or videos. It detects the file type (image or video), sends the necessary information to the corresponding API and displays success or error messages.
  - **Complexity:** Medium (14 nodes)

- **[1221-youtube-chapters-generator.json](workflows/1221-youtube-chapters-generator.json)**
  - **Description:** This workflow allows generating structured chapters for YouTube videos based on subtitles. It analyzes temporal content and creates an organized format.
  - **Complexity:** Medium (13 nodes)

- **[0129-twitter-banner-creator.json](workflows/0129-twitter-banner-creator.json)**
  - **Description:** This automatic flow allows downloading recent Twitter follower profiles, processing their avatar images (resizing and cropping), combining them with a background image via multi-stage composition, and finally uploading them as a banner using the OAuth1.0 API.
  - **Complexity:** Medium (12 nodes)

- **[0146-baserow-release-feed.json](workflows/0146-baserow-release-feed.json)**
  - **Description:** This automatic flow collects blog articles about 'release' from baserow.io and generates an XML response that can be used to feed feeds or webhooks.
  - **Complexity:** Medium (12 nodes)

- **[0423-spotify-youtube-sync.json](workflows/0423-spotify-youtube-sync.json)**
  - **Description:** This flow synchronizes songs between YouTube and Spotify playlists by adding only new ones without duplicates.
  - **Complexity:** Medium (12 nodes)

- **[0916-twitter-profile-banner-generator.json](workflows/0916-twitter-profile-banner-generator.json)**
  - **Description:** This automatic flow allows creating a dynamic banner for Twitter by combining the avatar images of the most recent followers with a background image, using the OAuth1.0 API.
  - **Complexity:** Medium (12 nodes)

- **[1222-wikipedia-summarization-fl.json](workflows/1222-wikipedia-summarization-fl.json)**
  - **Description:** This automatic flow uses Bright Data to extract information from Wikipedia and Google Gemini AI to format it into readable content and generate a concise summary.
  - **Complexity:** Medium (12 nodes)

- **[1454-create-dynamic-twitter-profile-banner.json](workflows/1454-create-dynamic-twitter-profile-banner.json)**
  - **Description:** This flow automates processes using Twitter/X with artificial intelligence and APIs.
  - **Complexity:** Medium (12 nodes)

- **[1504-twitter-virtual-ai-influencer.json](workflows/1504-twitter-virtual-ai-influencer.json)**
  - **Description:** This flow allows content generation using OpenAI/GPT, Twitter/X with artificial intelligence and scheduled APIs.
  - **Complexity:** Medium (12 nodes)

- **[2661-youtube-transcripciones-resumen.json](workflows/2661-youtube-transcripciones-resumen.json)**
  - **Description:** This automatic flow allows a user to send a YouTube URL via Webhook to get its video ID and then extract the video title and description. Subsequently, the video transcript is used along with gpt-4o-mini to generate structured summaries with definitions, features, implementation details and pros/cons, formatted in markdown.
  - **Complexity:** Medium (12 nodes)

- **[3023-ai-whatsapp-support-bot.json](workflows/3023-ai-whatsapp-support-bot.json)**
  - **Description:** This flow automates a customer support assistant on WhatsApp that uses artificial intelligence to answer questions based on the company's web content. It uses crawling and page analysis tools to obtain accurate information.
  - **Complexity:** Medium (12 nodes)

- **[0625-facebook_comments_flow.json](workflows/0625-facebook_comments_flow.json)**
  - **Description:** This flow obtains the latest messages and comments from posts on a Facebook page according to the initial configuration.
  - **Complexity:** Medium (11 nodes)

- **[1087-insta-chatbot-gpt.json](workflows/1087-insta-chatbot-gpt.json)**
  - **Description:** This flow allows integrating ChatGPT into Instagram via ManyChat to generate automated responses.
  - **Complexity:** Medium (11 nodes)

- **[2623-wordpress-xmlrpc-posting.json](workflows/2623-wordpress-xmlrpc-posting.json)**
  - **Description:** This automatic flow uses n8n along with the XML-RPC protocol to publish articles on WordPress.com.
  - **Complexity:** Medium (11 nodes)

- **[3212-cv-screening.json](workflows/3212-cv-screening.json)**
  - **Description:** This automatic flow downloads a CV from a URL, extracts its PDF content and sends the information along with a job description to OpenAI to obtain a structured evaluation that determines the candidate's profile based on the job requirements.
  - **Complexity:** Medium (11 nodes)

- **[0329-blog-medium-publisher.json](workflows/0329-blog-medium-publisher.json)**
  - **Description:** This automatic flow extracts WordPress blog content to publish on Medium using HTML and HTTP requests.
  - **Complexity:** Medium (10 nodes)

- **[0441-youtube-video-summarizer.json](workflows/0441-youtube-video-summarizer.json)**
  - **Description:** This automatic flow allows obtaining the transcript of a YouTube video and generating its summary using language models.
  - **Complexity:** Medium (10 nodes)

- **[0472-workflow-wordpress-tts.json](workflows/0472-workflow-wordpress-tts.json)**
  - **Description:** This automatic flow allows obtaining a WordPress article, generating its summary or transcript with AI and converting it to audio to be inserted as multimedia content in the same post.
  - **Complexity:** Medium (10 nodes)

- **[0858-tiktok-downloader-json.json](workflows/0858-tiktok-downloader-json.json)**
  - **Description:** Automatic to download TikTok videos without the water sticker.
  - **Complexity:** Medium (10 nodes)

- **[1090-upload-instagram-tiktok.json](workflows/1090-upload-instagram-tiktok.json)**
  - **Description:** This flow allows automatically uploading images to Instagram and TikTok using the same endpoint.
  - **Complexity:** Medium (10 nodes)

- **[3178-youtube-summarizer.json](workflows/3178-youtube-summarizer.json)**
  - **Description:** This flow automates the summarization of YouTube videos by extracting transcripts and using a language engine to generate concise summaries.
  - **Complexity:** Medium (10 nodes)

- **[0284-n8n-chat-conversational.json](workflows/0284-n8n-chat-conversational.json)**
  - **Description:** This flow allows the conversation to maintain context with the latest messages thanks to buffer memory storage. It uses search tools (SerpAPI) and Wikipedia to improve agent responses.
  - **Complexity:** Medium (9 nodes)

- **[0369-youtube-description-automation.json](workflows/0369-youtube-description-automation.json)**
  - **Description:** This automatic flow allows adding a predefined text to the description of all your YouTube videos, maintaining the existing original content and checking if updates are necessary.
  - **Complexity:** Medium (9 nodes)

- **[0474-update-youtube-descriptions.json](workflows/0474-update-youtube-descriptions.json)**
  - **Description:** This automatic flow allows inserting a specific text between two determined lines in the descriptions of all YouTube videos. First, all videos are collected, then for each one its ID is obtained and the text to be inserted is searched based on previously defined variables.
  - **Complexity:** Medium (9 nodes)

- **[0847-wp-ai-categorizer.json](workflows/0847-wp-ai-categorizer.json)**
  - **Description:** This flow automates the categorization of posts in WordPress using OpenAI language models.
  - **Complexity:** Medium (9 nodes)

- **[0883-n8n-ai-categorize-wordpress.json](workflows/0883-n8n-ai-categorize-wordpress.json)**
  - **Description:** This automatic template uses AI to assign a single category to multiple WordPress posts based on their title.
  - **Complexity:** Medium (9 nodes)

- **[1051-youtube-video-summarizer.json](workflows/1051-youtube-video-summarizer.json)**
  - **Description:** This flow uses Searchapi.io along with OpenAI models and advanced text splitting techniques to extract, process and generate a complete summary of specified YouTube video content.
  - **Complexity:** Medium (9 nodes)

- **[1223-line-gratitude-reminder.json](workflows/1223-line-gratitude-reminder.json)**
  - **Description:** This automated flow sends a personalized message generated by Azure OpenAI at 9:00 PM to motivate reflection on the positive aspects of the day via LINE.
  - **Complexity:** Medium (9 nodes)

- **[1441-auto-categorize-blog-posts-in-wordpress-using-ai.json](workflows/1441-auto-categorize-blog-posts-in-wordpress-using-ai.json)**
  - **Description:** This flow allows chatbot, automation using OpenAI/GPT, YouTube with artificial intelligence and APIs.
  - **Complexity:** Medium (9 nodes)

- **[2666-ft-news-resumen.json](workflows/2666-ft-news-resumen.json)**
  - **Description:** This automated flow daily collects financial news from FT.com, organizes it by specific content extraction using CSS Selectors, summarizes it with a Google Gemini model in HTML format and sends the structured summary to an Outlook inbox.
  - **Complexity:** Medium (8 nodes)

- **[0496-gmail-news-to-linkedin.json](workflows/0496-gmail-news-to-linkedin.json)**
  - **Description:** This automatic flow allows a user to receive Gmail newsletters and use OpenAI to identify main news, summarize them and generate LinkedIn posts with an intelligent style and subtle humor.
  - **Complexity:** Medium (7 nodes)

- **[1459-dynamically-generate-a-webpage-from-openai.json](workflows/1459-dynamically-generate-a-webpage-from-openai.json)**
  - **Description:** This flow allows chatbot, content generation using OpenAI/GPT, Webhook with artificial intelligence through webhooks and APIs.
  - **Complexity:** Medium (7 nodes)

- **[0072-medium-rss-feed.json](workflows/0072-medium-rss-feed.json)**
  - **Description:** This automatic flow processes N8N RSS feeds from Medium in batches.
  - **Complexity:** Medium (6 nodes)

- **[0305-certificate-email-batch.json](workflows/0305-certificate-email-batch.json)**
  - **Description:** This automatic flow reads a CSV file, splits it into batches and uses its content to send emails with previously generated certificates.
  - **Complexity:** Medium (6 nodes)

- **[0309-twitter-mentions-rocketchat.json](workflows/0309-twitter-mentions-rocketchat.json)**
  - **Description:** This flow checks Twitter every minute for mentions of '@n8n_io' and, if new, sends a message to RocketChat with the tweet text and its URL.
  - **Complexity:** Medium (6 nodes)

- **[0688-youtube-raindrop-sync.json](workflows/0688-youtube-raindrop-sync.json)**
  - **Description:** This automatic flow checks the specified YouTube playlist every 30 minutes and adds new videos to Raindrop as bookmarks with a title composed of the owner's name and video title, and the 'youtube' tag.
  - **Complexity:** Medium (6 nodes)

- **[1062-x-post-ai.json](workflows/1062-x-post-ai.json)**
  - **Description:** This automatic flow automatically publishes the latest YouTube videos on X/Twitter with text generated by ChatGPT.
  - **Complexity:** Medium (6 nodes)

- **[1076-youtube-promotion-x.json](workflows/1076-youtube-promotion-x.json)**
  - **Description:** This automatic flow checks every 30 minutes for new videos on a specific YouTube channel and uses ChatGPT to generate messages on X (formerly Twitter) that promote those videos, staying within character limits.
  - **Complexity:** Medium (6 nodes)

- **[1101-strapi-create-update.json](workflows/1101-strapi-create-update.json)**
  - **Description:** This automated flow allows creating an entry in Strapi (posts), saving its ID and then updating it with a specific slug.
  - **Complexity:** Medium (6 nodes)

- **[1485-post-new-youtube-videos-to-x.json](workflows/1485-post-new-youtube-videos-to-x.json)**
  - **Description:** This flow allows chatbot, content generation using OpenAI/GPT, Twitter/X, YouTube with artificial intelligence and scheduled APIs.
  - **Complexity:** Medium (6 nodes)

- **[2564-twitter-hilo-automatizacion.json](workflows/2564-twitter-hilo-automatizacion.json)**
  - **Description:** This automated flow uses Twitter tools and an OpenAI language model to generate coherent and interactive threads, maintaining conversational context.
  - **Complexity:** Medium (6 nodes)

- **[2659-content-creator-agent.json](workflows/2659-content-creator-agent.json)**
  - **Description:** This automatic flow uses the Tavily tool to search the internet for information on a specific topic provided by the user, and then uses an Anthropic Chat Model language model to generate well-structured HTML content for blogs. Connections ensure that a web search is performed first before asking the AI assistant to write the article.
  - **Complexity:** Medium (6 nodes)

- **[2710-youtube-sum-resumen.json](workflows/2710-youtube-sum-resumen.json)**
  - **Description:** This flow extracts text from a YouTube video using searchapi.io and summarizes it with LangChain and OpenAI to generate detailed summaries with example questions.
  - **Complexity:** Medium (6 nodes)

- **[0280-line-chatbot-agent.json](workflows/0280-line-chatbot-agent.json)**
  - **Description:** This automatic flow uses a LINE chatbot to handle messages, store context in buffer memory and access OpenAI's GPT-4o-mini model. It also integrates the SerpAPI tool for web search.
  - **Complexity:** Medium (5 nodes)

- **[0368-youtube-upload-create-playlist.json](workflows/0368-youtube-upload-create-playlist.json)**
  - **Description:** This automatic flow allows uploading a video to YouTube and creating a playlist, adding the ID of the newly uploaded video.
  - **Complexity:** Medium (5 nodes)

- **[0479-ideas-para-post.json](workflows/0479-ideas-para-post.json)**
  - **Description:** This automated flow reads ideas from a Google sheet, generates a post for the specified platform using OpenAI and, if it's Twitter, publishes it. Then it updates the sheet with the post text.
  - **Complexity:** Medium (5 nodes)

- **[0628-perplexity-research.json](workflows/0628-perplexity-research.json)**
  - **Description:** This automated flow searches for and extracts information related to a specific query using the Perplexity AI API, formatting the result to obtain clean content.
  - **Complexity:** Medium (5 nodes)

- **[0792-line-chatbot-memory-search.json](workflows/0792-line-chatbot-memory-search.json)**
  - **Description:** This automatic flow allows a LINE chatbot to maintain a contextualized conversation using buffer memory, integrating web search capability with SerpAPI and the GPT-4o-mini language model.
  - **Complexity:** Medium (5 nodes)

- **[0918-humantic-profile-management.json](workflows/0918-humantic-profile-management.json)**
  - **Description:** This automatic flow allows creating, updating and obtaining a Humantic AI profile using a LinkedIn URL as initial input.
  - **Complexity:** Medium (5 nodes)

- **[1027-facebook-long-lived-token.json](workflows/1027-facebook-long-lived-token.json)**
  - **Description:** This automatic flow obtains a long-lived Facebook access token from configured parameters and then uses it to obtain page tokens with application scope.
  - **Complexity:** Medium (5 nodes)

- **[1043-linkedin-url-discovery.json](workflows/1043-linkedin-url-discovery.json)**
  - **Description:** This flow searches for and extracts LinkedIn URLs in a specific Google sheet for each row.
  - **Complexity:** Medium (5 nodes)

- **[1470-generate-audio-from-text-using-openai-webhook-workflow.json](workflows/1470-generate-audio-from-text-using-openai-webhook-workflow.json)**
  - **Description:** This flow allows content generation using OpenAI/GPT, Webhook with artificial intelligence through webhooks and APIs.
  - **Complexity:** Medium (5 nodes)

- **[2534-news-twitter-post.json](workflows/2534-news-twitter-post.json)**
  - **Description:** This automatic flow searches for artificial intelligence news via a query to Perplexity AI, generates a formatted summary for Twitter/X and publishes it directly on the platform.
  - **Complexity:** Medium (5 nodes)

- **[0031-webflow-crear-y-actualizar.json](workflows/0031-webflow-crear-y-actualizar.json)**
  - **Description:** This flow allows creating and updating an item in the Webflow collection via manual activation.
  - **Complexity:** Low (4 nodes)

- **[0064-twitter-if-trigger.json](workflows/0064-twitter-if-trigger.json)**
  - **Description:** This automatic flow executes a fixed message on Twitter when activated via a manual click or by evaluating a numerical condition that depends on the iteration index ($runIndex), then passing to NoOp and Twitter nodes according to the results.
  - **Complexity:** Low (4 nodes)

- **[0134-tweet-image-jokes.json](workflows/0134-tweet-image-jokes.json)**
  - **Description:** This automatic flow executes a task every day at 5:00 PM to get graphic jokes from the Blablagues API and then publishes them on Twitter using images.
  - **Complexity:** Low (4 nodes)

- **[0195-ghost-post-automation.json](workflows/0195-ghost-post-automation.json)**
  - **Description:** This automatic flow allows creating a post in Ghost, updating its status to published and then obtaining information about the created post.
  - **Complexity:** Low (4 nodes)

- **[0312-wordpress-csv-export.json](workflows/0312-wordpress-csv-export.json)**
  - **Description:** This automated flow extracts and exports all WordPress articles to a CSV file.
  - **Complexity:** Low (4 nodes)

- **[0427-zoom-wordpress-schedule.json](workflows/0427-zoom-wordpress-schedule.json)**
  - **Description:** This automatic flow schedules a new Zoom meeting every 360 days and updates a WordPress post with its URL.
  - **Complexity:** Low (4 nodes)

- **[1246-twitter-banner-update.json](workflows/1246-twitter-banner-update.json)**
  - **Description:** This flow allows downloading an image from Unsplash and updating it as a banner on Twitter via HTTP requests.
  - **Complexity:** Low (4 nodes)

- **[1506-update-twitter-banner-using-http-request.json](workflows/1506-update-twitter-banner-using-http-request.json)**
  - **Description:** This flow automates processes using Twitter/X with artificial intelligence and APIs.
  - **Complexity:** Low (4 nodes)

- **[2608-youtube-transcript-extractor.json](workflows/2608-youtube-transcript-extractor.json)**
  - **Description:** This flow allows extracting and cleaning the transcribed text of a YouTube video using the RapidAPI.
  - **Complexity:** Low (4 nodes)

- **[0052-release-content-publisher.json](workflows/0052-release-content-publisher.json)**
  - **Description:** This automatic flow allows obtaining and publishing all content whose name starts with 'release' using Storyblok.
  - **Complexity:** Low (3 nodes)

- **[0530-workflow-bloqueo-medio-dev-to.json](workflows/0530-workflow-bloqueo-medio-dev-to.json)**
  - **Description:** This automated flow allows sending articles to both the Medium platform and the dev.to API via an HTTP request, using configured credentials for both actions.
  - **Complexity:** Low (3 nodes)

- **[0636-wp-post-automation.json](workflows/0636-wp-post-automation.json)**
  - **Description:** This automatic flow creates a new post in WordPress and immediately updates the content afterwards.
  - **Complexity:** Low (3 nodes)

- **[0657-linkedin-automation.json](workflows/0657-linkedin-automation.json)**
  - **Description:** This automated flow downloads an image from the specified URL and publishes that image on LinkedIn along with a predefined message.
  - **Complexity:** Low (3 nodes)

- **[1170-html-to-pdf-conversor.json](workflows/1170-html-to-pdf-conversor.json)**
  - **Description:** This automatic flow converts HTML content received in a webhook request into a PDF file and responds with it.
  - **Complexity:** Low (3 nodes)

- **[0306-twake-message-trigger.json](workflows/0306-twake-message-trigger.json)**
  - **Description:** This automatic flow is manually activated and sends an empty message to Twake without specifying content or channel.
  - **Complexity:** Low (2 nodes)

- **[0551-manual-aws-sns-trigger.json](workflows/0551-manual-aws-sns-trigger.json)**
  - **Description:** This manual flow allows sending a predefined message to a specific AWS SNS topic by clicking the 'execute' button.
  - **Complexity:** Low (2 nodes)

- **[0553-aws-ses-email.json](workflows/0553-aws-ses-email.json)**
  - **Description:** This automatic flow allows sending a predefined email via AWS SES when manually executed.
  - **Complexity:** Low (2 nodes)

- **[0555-manual-aws-lambda-test.json](workflows/0555-manual-aws-lambda-test.json)**
  - **Description:** This manual flow allows triggering a specific AWS Lambda via a click action.
  - **Complexity:** Low (2 nodes)

- **[0583-wordpress-get-all.json](workflows/0583-wordpress-get-all.json)**
  - **Description:** This flow allows manually executing an action that obtains all articles from a WordPress instance via its API credentials.
  - **Complexity:** Low (2 nodes)

- **[0647-contentful-get-all.json](workflows/0647-contentful-get-all.json)**
  - **Description:** This automatic flow allows obtaining all content items from a Contentful instance via a manual trigger.
  - **Complexity:** Low (2 nodes)

- **[0687-medium-publication.json](workflows/0687-medium-publication.json)**
  - **Description:** This flow allows publishing articles to a Medium publication.
  - **Complexity:** Low (2 nodes)

- **[0746-strava-twitter-tweet.json](workflows/0746-strava-twitter-tweet.json)**
  - **Description:** This automatic flow monitors new cycling activities on Strava and publishes a tweet on Twitter with details about the distance traveled and the exercise name.
  - **Complexity:** Low (2 nodes)

- **[0533-digitalocean-create-droplet.json](workflows/0533-digitalocean-create-droplet.json)**
  - **Description:** This automatic flow creates a Droplet instance in DigitalOcean using the specified parameters and authenticating with a personal access token.
  - **Complexity:** Low (1 nodes)


### E-commerce and Payments

- **[0826-ai-woocommerce-support-agent.json](workflows/0826-ai-woocommerce-support-agent.json)**
  - **Description:** This automated flow implements an AI assistant with n8n and WooCommerce to manage customer queries about their orders, ensuring privacy through email encryption and integrating functions such as DHL.
  - **Complexity:** High (40 nodes)

- **[3077-shopify-to-d365-sync.json](workflows/3077-shopify-to-d365-sync.json)**
  - **Description:** This flow synchronizes Shopify orders with Dynamics 365 Business Central by creating orders and invoices. It detects if orders are from POS or web to generate invoices or orders respectively, verifies customer existence and creates new ones if they are not in BC. It handles multi-store locations and adds taxes and discounts as lines.
  - **Complexity:** High (39 nodes)

- **[0487-shopify-fulfillment-auto.json](workflows/0487-shopify-fulfillment-auto.json)**
  - **Description:** This automatic flow seeks to filter and obtain pending fulfillment orders in Shopify for digital downloads or gift cards.
  - **Complexity:** Medium (13 nodes)

- **[2640-shopify-orders-to-baserow.json](workflows/2640-shopify-orders-to-baserow.json)**
  - **Description:** This automatic flow executes a daily GraphQL query to obtain Shopify orders and inserts them into a Baserow-based table, extracting UTM parameters from the first visit. Only orders where the 'Campaign' field is present are processed.
  - **Complexity:** Medium (12 nodes)

- **[2558-bee-hiiv-gumroad-subscribers.json](workflows/2558-bee-hiiv-gumroad-subscribers.json)**
  - **Description:** This flow automates the addition of subscribers to a Beehiiv newsletter every time a sale is made on Gumroad.
  - **Complexity:** Medium (10 nodes)

- **[0002-Gumroad-MailerLite-trigger.json](workflows/0002-Gumroad-MailerLite-trigger.json)**
  - **Description:** This automatic flow adds a subscriber to MailerLite when a sale occurs on Gumroad and immediately assigns them to a specific group.
  - **Complexity:** Medium (8 nodes)

- **[0403-stripe-checkout-filters.json](workflows/0403-stripe-checkout-filters.json)**
  - **Description:** This automatic flow retrieves all Stripe checkout sessions from the last month and allows filtering them based on custom fields such as nickname or job_title.
  - **Complexity:** Medium (7 nodes)

- **[2650-shopify-odoo-customer-sync.json](workflows/2650-shopify-odoo-customer-sync.json)**
  - **Description:** This flow automatically synchronizes new Shopify customers with contacts in Odoo, first checking if a matching contact already exists and creating it if not found.
  - **Complexity:** Medium (5 nodes)

- **[0260-woo-product-flow.json](workflows/0260-woo-product-flow.json)**
  - **Description:** This automatic flow allows creating a product in WooCommerce, updating its stock and then obtaining the created product.
  - **Complexity:** Low (4 nodes)

- **[0027-chargebee-nuevo-cliente.json](workflows/0027-chargebee-nuevo-cliente.json)**
  - **Description:** This automatic flow allows creating a new customer in Chargebee by executing the manual task.
  - **Complexity:** Low (2 nodes)

- **[0140-onfleet-shopify-task.json](workflows/0140-onfleet-shopify-task.json)**
  - **Description:** This automatic flow synchronizes the creation of a new fulfillment in Shopify with the corresponding generation of a task in Onfleet.
  - **Complexity:** Low (2 nodes)

- **[0167-shopify-onfleet-tags-sync.json](workflows/0167-shopify-onfleet-tags-sync.json)**
  - **Description:** This automatic flow updates a product's tags in Shopify every time a delay is detected in an Onfleet task.
  - **Complexity:** Low (2 nodes)

- **[0535-pay-pal-batch-operation.json](workflows/0535-pay-pal-batch-operation.json)**
  - **Description:** This flow executes an operation on the PayPal account using the provided batch ID.
  - **Complexity:** Low (2 nodes)

- **[0585-shopify-get-all-records.json](workflows/0585-shopify-get-all-records.json)**
  - **Description:** This flow manually executes the 'execute' trigger which then obtains all records from a Shopify account.
  - **Complexity:** Low (2 nodes)

- **[0587-paddle-coupon-creator.json](workflows/0587-paddle-coupon-creator.json)**
  - **Description:** This automatic flow allows creating a coupon offer in Paddle using specific parameters.
  - **Complexity:** Low (2 nodes)

- **[0049-chargebee-event-trigger.json](workflows/0049-chargebee-event-trigger.json)**
  - **Description:** This automatic flow receives updates for any event in Chargebee.
  - **Complexity:** Low (1 nodes)

- **[0495-gumroad-sale-trigger.json](workflows/0495-gumroad-sale-trigger.json)**
  - **Description:** This automatic flow is activated when a sale occurs on Gumroad.
  - **Complexity:** Low (1 nodes)

- **[0584-shopify-order-trigger.json](workflows/0584-shopify-order-trigger.json)**
  - **Description:** This active flow is triggered when a new order is created in Shopify via webhook.
  - **Complexity:** Low (1 nodes)

- **[1531-Shopify_Agent.json](workflows/1531-Shopify_Agent.json)**
  - **Description:** Shopify agent that interacts with the Shopify API to manage orders and products, including uploading product data to Qdrant.
  - **Complexity:** High (30 nodes)

- **[1532-Ecommerce_Assistant.json](workflows/1532-Ecommerce_Assistant.json)**
  - **Description:** Customer service assistant for an eCommerce that answers product queries using a PostgreSQL database.
  - **Complexity:** Medium (5 nodes)

- **[1548-Ecommerce_Agent_v1.json](workflows/1548-Ecommerce_Agent_v1.json)**
  - **Description:** eCommerce agent that processes WhatsApp messages, manages chat history with Redis, and uses an AI agent to answer product queries.
  - **Complexity:** High (30 nodes)

- **[1549-Ecommerce_Agent_v2.json](workflows/1549-Ecommerce_Agent_v2.json)**
  - **Description:** eCommerce agent that processes WhatsApp messages, manages chat history with Redis, and uses an AI agent to answer product queries.
  - **Complexity:** High (30 nodes)

- **[1554-Agente_Ecommerce_v3.json](workflows/1554-Agente_Ecommerce_v3.json)**
  - **Description:** eCommerce agent that processes WhatsApp messages, manages chat history with Redis, and uses an AI agent to answer product queries.
  - **Complexity:** High (30 nodes)

- **[1555-Agente_Ecommerce_v3_subflujo.json](workflows/1555-Agente_Ecommerce_v3_subflujo.json)**
  - **Description:** Subflow of eCommerce agent that processes product data and uploads it to a vector database.
  - **Complexity:** Medium (10 nodes)


### Artificial Intelligence and Natural Language Processing (NLP)

- **[2667-auto-doc-gpt-docsify.json](workflows/2667-auto-doc-gpt-docsify.json)**
  - **Description:** This automatic flow generates Markdown documentation for n8n workflows using GPT and Docsify, allowing the creation of interactive pages with visual schemas (Mermaid) that describe each node.
  - **Complexity:** High (60 nodes)

- **[3063-animated_stories_generator.json](workflows/3063-animated_stories_generator.json)**
  - **Description:** This flow creates animated stories using GPT-4o-mini to generate prompts, Midjourney to create images and Kling to generate videos, then combines the videos in Creatomate.
  - **Complexity:** High (51 nodes)

- **[2924-hacker_news_video_creator.json](workflows/2924-hacker_news_video_creator.json)**
  - **Description:** This flow automates the creation of videos from Hacker News articles. It collects articles, analyzes them to determine their relevance, generates images with Leonardo AI and RunwayML, and creates a video with Creatomate.
  - **Complexity:** High (48 nodes)

- **[2996-perplexity_to_html.json](workflows/2996-perplexity_to_html.json)**
  - **Description:** This flow automates the creation of an HTML page from Perplexity research, structuring and styling with Tailwind CSS.
  - **Complexity:** High (47 nodes)

- **[2777-encuesta-analisis.json](workflows/2777-encuesta-analisis.json)**
  - **Description:** This flow automates obtaining surveys and analysis using OpenAI and Qdrant to extract insights through clustering and embeddings.
  - **Complexity:** High (42 nodes)

- **[2828-organizador-tags.json](workflows/2828-organizador-tags.json)**
  - **Description:** This automatic flow organizes workflows into specific folders based on tags. First, it logs into n8n, extracts tags from personal projects, allows selecting them via a form and then moves workflows to the corresponding folders or creates new ones if necessary.
  - **Complexity:** High (40 nodes)

- **[3108-subworkflow-dependency-graph.json](workflows/3108-subworkflow-dependency-graph.json)**
  - **Description:** This flow automates the creation of a dependency graph between workflows in n8n and automatically assigns tags based on detected relationships. It analyzes flows to identify which ones are called by others, visualizes these relationships and creates new tags if changes are detected.
  - **Complexity:** High (40 nodes)

- **[0787-n8n-ai-demo-multifunction.json](workflows/0787-n8n-ai-demo-multifunction.json)**
  - **Description:** This automatic flow uses the n8n platform to build a multifunctional AI system that includes PDF processing via embeddings and text splitting, as well as a chatbot with QA based on documents using the GPT-4o model. It also integrates a functionality to schedule appointments.
  - **Complexity:** High (39 nodes)

- **[0912-adaptive-rag-strategy.json](workflows/0912-adaptive-rag-strategy.json)**
  - **Description:** This flow analyzes and classifies queries into specific categories (Factual, Analytical, Opinion or Contextual) to apply adaptive retrieval and artificial intelligence strategies that optimize the obtaining of relevant information.
  - **Complexity:** High (39 nodes)

- **[2776-pdf-pinecone-reserva.json](workflows/2776-pdf-pinecone-reserva.json)**
  - **Description:** Flow that includes downloading a PDF, embedding it and storing it in Pinecone, in addition to an appointment booking capability via Google Calendar using language agents such as GPT-4o and Anthropic.
  - **Complexity:** High (39 nodes)

- **[2823-anthropic-batch-processing.json](workflows/2823-anthropic-batch-processing.json)**
  - **Description:** This automatic flow sends multiple prompts simultaneously to the Anthropic Claude Batch API, checks their status and processes the results using memory nodes to maintain context.
  - **Complexity:** High (39 nodes)

- **[2755-social-media-crawler.json](workflows/2755-social-media-crawler.json)**
  - **Description:** This flow extracts social media information from websites using text and URL retrieval tools. It navigates pages, obtains social links and organizes them in JSON format.
  - **Complexity:** High (38 nodes)

- **[2771-tax-code-ai-assistant.json](workflows/2771-tax-code-ai-assistant.json)**
  - **Description:** This flow automates the creation of a legal chatbot assistant specialized in Texan tax codes. It downloads, processes and stores PDF documents in Qdrant using Mistral.ai embeddings to allow advanced searches.
  - **Complexity:** High (38 nodes)

- **[1150-spotify-playlist-classifier.json](workflows/1150-spotify-playlist-classifier.json)**
  - **Description:** This automatic flow allows classifying and adding Spotify tracks to multiple playlists based on their characteristics and playback history using the Claude 3.5 model.
  - **Complexity:** High (37 nodes)

- **[2807-automatiza-categorizacion-outlook.json](workflows/2807-automatiza-categorizacion-outlook.json)**
  - **Description:** This flow automates the categorization of emails in Outlook using an artificial intelligence agent. It extracts the email body, processes it to remove HTML and then sends it to an Ollama language model to assign categories. If it fails, it logs the error. Depending on the resulting category, it moves emails to different folders such as 'Junk', 'Receipt', 'SaaS', 'Community', 'Business' or 'Action'.
  - **Complexity:** High (36 nodes)

- **[3150-whatsapp-ai-responder.json](workflows/3150-whatsapp-ai-responder.json)**
  - **Description:** This automatic flow manages WhatsApp messages using AI to respond professionally. It analyzes different types of messages (text, audio, video e image), processes them with tools such as Google Gemini and Wikipedia, and generates timely responses.
  - **Complexity:** High (35 nodes)

- **[3202-whatsapp-bot-process.json](workflows/3202-whatsapp-bot-process.json)**
  - **Description:** This automatic flow processes WhatsApp messages, handles different types such as audio, video and image using Google Gemini for transcription and analysis, and uses an artificial intelligence agent to respond.
  - **Complexity:** High (35 nodes)

- **[2545-visual-regression-testing.json](workflows/2545-visual-regression-testing.json)**
  - **Description:** This automatic flow allows performing visual regression tests on web pages using Apify to capture images and visual language models such as Gemini to detect changes between versions.
  - **Complexity:** High (34 nodes)

- **[2794-visual-regression-test-flow.json](workflows/2794-visual-regression-test-flow.json)**
  - **Description:** Automated flow to perform visual regression tests on websites using Google Gemini and Apify. It generates base images, compares them with recent captures and reports detected changes via Linear.
  - **Complexity:** High (34 nodes)

- **[3076-ai-seo-keyword-automation.json](workflows/3076-ai-seo-keyword-automation.json)**
  - **Description:** This automatic flow uses artificial intelligence to perform SEO keyword research. It includes topic expansion, competitor analysis, metrics such as search volume and CPC, and generates an optimized final strategy.
  - **Complexity:** High (34 nodes)

- **[3237-ai_magic_position.json](workflows/3237-ai_magic_position.json)**
  - **Description:** This flow includes an AI agent with memory and vector retrieval capabilities, connected to OpenAI and HTTP tools to position flows.
  - **Complexity:** High (34 nodes)

- **[0715-ai-calendar-mcp.json](workflows/0715-ai-calendar-mcp.json)**
  - **Description:** This n8n workflow uses an AI agent with OpenAI to manage conversational interactions related to the Google Calendar. It allows creating, searching, updating and deleting events, as well as modifying text between uppercase and lowercase using tools that respond to commands.
  - **Complexity:** High (32 nodes)

- **[2894-onboarding-clientes.json](workflows/2894-onboarding-clientes.json)**
  - **Description:** This flow automates the onboarding of new customers by sending a welcome email and scheduling a call with an assigned account manager.
  - **Complexity:** High (31 nodes)

- **[0718-crypto-news-sentiment-bot.json](workflows/0718-crypto-news-sentiment-bot.json)**
  - **Description:** This automatic flow analyzes the user's query to extract a keyword, searches for related news in multiple cryptocurrency RSS feeds and uses GPT-4o to synthesize information and evaluate market sentiment.
  - **Complexity:** High (30 nodes)

- **[2954-financial-documents-assistant.json](workflows/2954-financial-documents-assistant.json)**
  - **Description:** This flow monitors a local directory for financial documents and synchronizes changes with Qdrant using Mistral.ai to create a question and answer assistant.
  - **Complexity:** High (29 nodes)

- **[3282-analisis_medios_gemini.json](workflows/3282-analisis_medios_gemini.json)**
  - **Description:** This flow uses different methodologies to analyze media such as images and PDFs using artificial intelligence agents. It includes specific routes for individual and batch image analysis, use of custom prompts, transformation to base64 format and direct calls to the Gemini API.
  - **Complexity:** High (28 nodes)

- **[0779-rag-movie-recom-qdrant-openai.json](workflows/0779-rag-movie-recom-qdrant-openai.json)**
  - **Description:** This automatic flow implements an AI chatbot based on RAG to recommend movies using Qdrant as vector storage and OpenAI for embeddings and interaction.
  - **Complexity:** High (27 nodes)

- **[0877-rag-peliculas-recomendacion-qdrant.json](workflows/0877-rag-peliculas-recomendacion-qdrant.json)**
  - **Description:** This automatic flow allows a chatbot to recommend movies by using Qdrant vector storage and embeddings generated with OpenAI for user query analysis.
  - **Complexity:** High (27 nodes)

- **[1112-openai-n8n-examples.json](workflows/1112-openai-n8n-examples.json)**
  - **Description:** This n8n flow contains examples of how to use different OpenAI models and APIs to generate summaries (TLDR), translate text, create prompts for images and more.
  - **Complexity:** High (27 nodes)

- **[1395-call-processor.json](workflows/1395-call-processor.json)**
  - **Description:** Processes call recordings and extracts information.
  - **Complexity:** High (27 nodes)

- **[3100-openai-examples.json](workflows/3100-openai-examples.json)**
  - **Description:** This flow uses different OpenAI models such as ChatGPT to summarize and translate text, Whisper-1 for audio transcription and DALLE-2 to generate images from text descriptions.
  - **Complexity:** High (27 nodes)

- **[0821-email-ai-auto-responder.json](workflows/0821-email-ai-auto-responder.json)**
  - **Description:** This automatic flow analyzes incoming emails using DeepSeek and OpenAI to summarize them and identify the topic. If the classification detects that it is a request about the company, a professionally structured response is generated based on information from Qdrant.
  - **Complexity:** High (26 nodes)

- **[1007-comprador-personalizado-IA-RAG.json](workflows/1007-comprador-personalizado-IA-RAG.json)**
  - **Description:** This flow uses OpenAI and RAG to create a personalized assistant that answers product queries or general business information.
  - **Complexity:** High (25 nodes)

- **[2993-paul_graham_essays_milvus.json](workflows/2993-paul_graham_essays_milvus.json)**
  - **Description:** This flow automates the extraction and storage of Paul Graham's articles in Milvus, using OpenAI to generate responses with contextual citations.
  - **Complexity:** High (25 nodes)

- **[3139-AppointmentQualifierAI.json](workflows/3139-AppointmentQualifierAI.json)**
  - **Description:** Form flow that uses artificial intelligence to qualify appointment requests and manages their approval through integrated forms in n8n.
  - **Complexity:** High (25 nodes)

- **[0905-whatsapp-chatbot-rag.json](workflows/0905-whatsapp-chatbot-rag.json)**
  - **Description:** This automatic flow configures an AI-powered WhatsApp chatbot that uses RAG (Retrieval-Augmented Generation) with OpenAI to maintain contextualized conversations.
  - **Complexity:** High (24 nodes)

- **[0914-website-chatbot-n8n.json](workflows/0914-website-chatbot-n8n.json)**
  - **Description:** This automatic flow allows an n8n chatbot to maintain conversations with customers, check agenda availability via Microsoft Outlook API and send structured responses. The AI agent uses the GPT-4o model to process queries and make decisions about appointments or message sending.
  - **Complexity:** High (24 nodes)

- **[0936-ai-grant-tracker.json](workflows/0936-ai-grant-tracker.json)**
  - **Description:** This automated flow allows filtering and analyzing AI-related grant opportunities on grants.gov. It uses nodes to deduplicate via a tracking system, requests detailed information about each grant via the grants.gov API and incorporates OpenAI generative models to determine eligibility and facilitate the process.
  - **Complexity:** High (24 nodes)

- **[1452-complete-business-whatsapp-ai-powered-openai.json](workflows/1452-complete-business-whatsapp-ai-powered-openai.json)**
  - **Description:** This flow allows chatbot using OpenAI/GPT, Webhook, WhatsApp with artificial intelligence through webhooks and APIs.
  - **Complexity:** High (24 nodes)

- **[0814-elevenlabs-voice-rag-chatbot.json](workflows/0814-elevenlabs-voice-rag-chatbot.json)**
  - **Description:** This automatic flow allows an ElevenLabs chatbot to maintain voice conversations with customers using vectorized documents and contextualized memory.
  - **Complexity:** High (23 nodes)

- **[2749-spotify-downloads-manager.json](workflows/2749-spotify-downloads-manager.json)**
  - **Description:** This automatic flow manages a Spotify playlist called 'Downloads'. It searches for the most recent songs that the user has marked as favorites and adds them to the playlist, keeping only a defined number of songs. If the playlist does not exist, it creates it. If it already exists, it deletes the oldest songs if the limit is exceeded.
  - **Complexity:** High (23 nodes)

- **[2757-automatiza-rfp.json](workflows/2757-automatiza-rfp.json)**
  - **Description:** Automatic flow to generate RFP responses using Webhooks, Google Docs and OpenAI. It receives an RFP document, extracts questions, processes them with AI and inserts the responses into a Google Docs document.
  - **Complexity:** High (23 nodes)

- **[0895-chat-pdf-ai-citas.json](workflows/0895-chat-pdf-ai-citas.json)**
  - **Description:** This automatic flow allows a chatbot to analyze PDF documents using OpenAI embeddings and retrieve relevant information with exact citations when queried.
  - **Complexity:** High (22 nodes)

- **[0946-dynamically_switch_llms_customer_support.json](workflows/0946-dynamically_switch_llms_customer_support.json)**
  - **Description:** This n8n flow dynamically selects and uses different language models (such as OpenAI) based on an index to generate versatile responses and iterate until it finds one that meets specified criteria, such as polite tone.
  - **Complexity:** High (22 nodes)

- **[0780-milvus-paul-graham-essays.json](workflows/0780-milvus-paul-graham-essays.json)**
  - **Description:** This flow allows creating a knowledge base with OpenAI embeddings from recent Paul Graham essays, storing the vectors in a Milvus collection.
  - **Complexity:** High (21 nodes)

- **[0932-podcast-summary-flow.json](workflows/0932-podcast-summary-flow.json)**
  - **Description:** This automatic flow allows users to receive a daily summary of top podcasts by specific genre via transcription and artificial intelligence.
  - **Complexity:** High (21 nodes)

- **[1103-plex-qbittorrent-automation.json](workflows/1103-plex-qbittorrent-automation.json)**
  - **Description:** This flow automates speed control and download management in QBittorrent based on Plex webhook events, allowing configuring speed limits or performing specific actions such as pausing/resuming torrents based on the action received.
  - **Complexity:** High (21 nodes)

- **[2893-imagen-style-transfer.json](workflows/2893-imagen-style-transfer.json)**
  - **Description:** This flow generates images based on a source image style using Google Imagen 3.0 and Gemini 2.0 to describe the style. Users provide a source image URL and a target image prompt via a form, then the input is validated and the source image is downloaded. The image is analyzed with Gemini 2.0 to obtain a detailed description of the visual style, which is combined with the user's prompt to generate new images with Imagen 3.0. Generated images are uploaded to Cloudinary and sent to email if the user specifies it.
  - **Complexity:** High (21 nodes)

- **[3075-video-narration-ai.json](workflows/3075-video-narration-ai.json)**
  - **Description:** This flow automates the creation of a narrative script for videos using multimodal artificial intelligence. It downloads a video, extracts evenly distributed frames, processes them with a large language model (LLM) to generate descriptive texts and then converts that text into audio.
  - **Complexity:** High (21 nodes)

- **[3203-video-narration-generator.json](workflows/3203-video-narration-generator.json)**
  - **Description:** This flow automates the creation of a narrative script for videos using OpenAI and then generates audio from that script.
  - **Complexity:** High (21 nodes)

- **[3317-agendamiento-citas-ai.json](workflows/3317-agendamiento-citas-ai.json)**
  - **Description:** This automatic flow uses Gmail and Google Calendar to analyze emails requesting an appointment, check calendar availability and propose free times via an artificial intelligence agent.
  - **Complexity:** High (21 nodes)

- **[2795-banco-estado-pdf-to-markdown.json](workflows/2795-banco-estado-pdf-to-markdown.json)**
  - **Description:** This flow automates the conversion of a PDF bank statement in image format to structured text in markdown using Google Gemini and advanced OCR.
  - **Complexity:** High (20 nodes)

- **[3012-web-query-semantic-re-ranking.json](workflows/3012-web-query-semantic-re-ranking.json)**
  - **Description:** This flow automates performing web queries and semantically re-ranking results using Brave and Google Gemini to improve relevance.
  - **Complexity:** High (20 nodes)

- **[3159-trustpilot-sentiment.json](workflows/3159-trustpilot-sentiment.json)**
  - **Description:** This flow extracts and analyzes Trustpilot reviews using DeepSeek to obtain detailed information and then OpenAI to evaluate sentiment.
  - **Complexity:** High (20 nodes)

- **[0795-realtime-meeting-transcriber.json](workflows/0795-realtime-meeting-transcriber.json)**
  - **Description:** This flow automates real-time meeting transcription using Recall.ai and integrates generated notes with an OpenAI chatbot for insights.
  - **Complexity:** High (19 nodes)

- **[2531-etsy-product-scraper.json](workflows/2531-etsy-product-scraper.json)**
  - **Description:** This automatic flow uses Bright Data Web Unlocker to perform advanced scraping on Etsy and extracts detailed product information using Google Gemini Flash based on the results obtained.
  - **Complexity:** High (19 nodes)

- **[2943-auto-label-gmail.json](workflows/2943-auto-label-gmail.json)**
  - **Description:** This flow automates the assignment of labels to new Gmail messages using artificial intelligence. It collects emails, processes them with a language model to determine appropriate labels and then applies them.
  - **Complexity:** High (19 nodes)

- **[3342-web_agent_airtop.json](workflows/3342-web_agent_airtop.json)**
  - **Description:** This flow configures a web agent that uses Airtop to interact with a browser window, including opening URLs, clicking and querying web pages following user instructions. The agent also uses Anthropic's Claude 3.5 to process interactions.
  - **Complexity:** High (19 nodes)

- **[0333-bored-api-activity-tool.json](workflows/0333-bored-api-activity-tool.json)**
  - **Description:** This flow allows an AI agent to call a subflow to extract information about type and number of participants, then use that information to filter activities via the Bored API and return the combined result in a chatbot response.
  - **Complexity:** High (18 nodes)

- **[0713-bright-data-gemini-chat-enhancement.json](workflows/0713-bright-data-gemini-chat-enhancement.json)**
  - **Description:** This flow allows Gemini AI to incorporate real-time search results from Google, Bing or Yandex to improve chatbot responses.
  - **Complexity:** High (18 nodes)

- **[0937-detect-hallucinations-ollama.json](workflows/0937-detect-hallucinations-ollama.json)**
  - **Description:** This flow analyzes texts to identify incorrect statements using a specialized Ollama model called bespoke-minicheck. It processes the text by splitting it into sentences maintaining structural elements such as dates and lists, then extracts 'facts' for verification using LLM chains.
  - **Complexity:** High (18 nodes)

- **[2880-calendario_openai_report.json](workflows/2880-calendario_openai_report.json)**
  - **Description:** This flow automates the research of assistants and companies using OpenAI API, collects Google calendar information and sends a detailed report by email.
  - **Complexity:** High (18 nodes)

- **[3323-hr-automatizacion.json](workflows/3323-hr-automatizacion.json)**
  - **Description:** This automatic flow manages the automation of the personnel selection process by extracting key information from CVs, analyzing it with artificial intelligence and consolidating results in a spreadsheet.
  - **Complexity:** High (18 nodes)

- **[0876-image-search-workflow.json](workflows/0876-image-search-workflow.json)**
  - **Description:** This automatic flow allows searching for images based on detected objects using artificial intelligence, CDN and ElasticSearch to efficiently store and query results.
  - **Complexity:** High (17 nodes)

- **[0950-dsp-ai-tutor.json](workflows/0950-dsp-ai-tutor.json)**
  - **Description:** This n8n flow acts as a tutoring assistant for signal processing students, using OpenAI and Google Gemini models to guide them interactively through theoretical explanations, numerical solutions or memory references.
  - **Complexity:** High (17 nodes)

- **[0958-image-caption-overlay.json](workflows/0958-image-caption-overlay.json)**
  - **Description:** This automatic flow downloads an image using HTTP Request, resizes it to optimize it for AI and adds a punny caption generated by Gemini 1.5 Pro.
  - **Complexity:** High (16 nodes)

- **[1439-ask-questions-about-a-pdf-using-ai.json](workflows/1439-ask-questions-about-a-pdf-using-ai.json)**
  - **Description:** This flow allows chatbot using OpenAI/GPT, Webhook with artificial intelligence through webhooks and APIs.
  - **Complexity:** High (16 nodes)

- **[2793-image-caption-generator.json](workflows/2793-image-caption-generator.json)**
  - **Description:** This flow automates the generation of image captions using the Gemini model and applies them visually.
  - **Complexity:** High (16 nodes)

- **[2830-outlook-calendar-agent.json](workflows/2830-outlook-calendar-agent.json)**
  - **Description:** This flow uses an artificial intelligence agent to handle queries related to the Outlook calendar. The user can ask questions about calendar events and the agent, equipped with Outlook tools, will respond appropriately.
  - **Complexity:** High (16 nodes)

- **[3072-ollama-llm-router.json](workflows/3072-ollama-llm-router.json)**
  - **Description:** This flow configures a private and local LLM automatic route using Ollama to dynamically select the most appropriate model based on user input.
  - **Complexity:** High (16 nodes)

- **[0546-thehive-email-iocs.json](workflows/0546-thehive-email-iocs.json)**
  - **Description:** This automatic flow processes incoming emails via IMAP, analyzes them with Cortex to detect indicators of compromise (IoCs), and creates corresponding observables in TheHive for each type of IoC identified.
  - **Complexity:** Medium (15 nodes)

- **[0662-brave-search-chatbot.json](workflows/0662-brave-search-chatbot.json)**
  - **Description:** This workflow implements a chatbot that uses GPT-4o and MCP tools to perform web searches in Brave, maintaining contextualized memory.
  - **Complexity:** Medium (15 nodes)

- **[0813-voice-ai-chat.json](workflows/0813-voice-ai-chat.json)**
  - **Description:** This automatic flow integrates Webhook for real-time voice input, contextualized memory management with models such as Google Gemini and ElevenLabs.
  - **Complexity:** Medium (15 nodes)

- **[1163-strava_ai_coaching_analysis.json](workflows/1163-strava_ai_coaching_analysis.json)**
  - **Description:** This automated flow analyzes sports activities from Strava using a conversational AI based on Google Gemini to offer personalized triathlon coaching and sends a formatted summary by email.
  - **Complexity:** Medium (15 nodes)

- **[1219-paul_graham_essays_resumer.json](workflows/1219-paul_graham_essays_resumer.json)**
  - **Description:** This automated flow extracts the URLs of recent Paul Graham essays from a list of articles, then obtains the full text of each essay and summarizes it using GPT.
  - **Complexity:** Medium (15 nodes)

- **[2549-semanal-shodan-thehive.json](workflows/2549-semanal-shodan-thehive.json)**
  - **Description:** This automatic flow schedules a weekly scan of IP addresses and their specific ports using Shodan. If it finds unexpected services or behaviors, it generates an alert in TheHive for management.
  - **Complexity:** Medium (15 nodes)

- **[2550-3d-character-generation.json](workflows/2550-3d-character-generation.json)**
  - **Description:** This automatic flow creates 3D rotation videos and figurine models from images, using PiAPI APIs to generate character designs via Midjourney and integrate them with tools like GPT-4o.
  - **Complexity:** Medium (15 nodes)

- **[2677-reddit-n8n-monitor.json](workflows/2677-reddit-n8n-monitor.json)**
  - **Description:** This flow automates the monitoring of Reddit posts related to n8n, using OpenAI to classify and summarize relevant ones.
  - **Complexity:** Medium (15 nodes)

- **[2696-country_capitals_fiction.json](workflows/2696-country_capitals_fiction.json)**
  - **Description:** This flow uses ChatGPT to answer questions about fictional country capitals. The user can ask for a list of countries or the capital of a specific country.
  - **Complexity:** Medium (15 nodes)

- **[2809-seo-ai-keywords-generator.json](workflows/2809-seo-ai-keywords-generator.json)**
  - **Description:** Flow that generates SEO keywords using an artificial intelligence agent based on the ideal customer profile (ICP).
  - **Complexity:** Medium (15 nodes)

- **[3147-reddit-n8n-analizador.json](workflows/3147-reddit-n8n-analizador.json)**
  - **Description:** This flow collects and analyzes recent Reddit posts related to n8n, using OpenAI to classify and summarize the posts.
  - **Complexity:** Medium (15 nodes)

- **[3188-ai-voice-chat.json](workflows/3188-ai-voice-chat.json)**
  - **Description:** This flow implements a voice chatbot that uses Webhook, Memory Manager, OpenAI, Google Gemini and ElevenLabs to maintain a contextualized conversation with the user. The process includes transcribing audio, storing and retrieving context, generating responses with artificial intelligence and converting them to audio.
  - **Complexity:** Medium (15 nodes)

- **[0461-milvus-rag-chatbot-flow.json](workflows/0461-milvus-rag-chatbot-flow.json)**
  - **Description:** This automatic flow allows a LINE chatbot to maintain a contextualized conversation using PDF documents inserted in Milvus and RAG queries with Cohere embeddings.
  - **Complexity:** Medium (14 nodes)

- **[0893-chat-ai-contexto.json](workflows/0893-chat-ai-contexto.json)**
  - **Description:** This automated flow allows maintaining a contextualized conversation with the OpenAI assistant by managing previous messages.
  - **Complexity:** Medium (14 nodes)

- **[1450-chatgpt-automatic-code-review-in-gitlab-mr.json](workflows/1450-chatgpt-automatic-code-review-in-gitlab-mr.json)**
  - **Description:** This flow allows chatbot using OpenAI/GPT, Webhook with artificial intelligence through webhooks and APIs.
  - **Complexity:** Medium (14 nodes)

- **[2632-line-chatbot-memory.json](workflows/2632-line-chatbot-memory.json)**
  - **Description:** This automatic flow allows a LINE chatbot to maintain contextualized conversations using the GPT-4o-mini model and access information through tools such as Wikipedia, Google Calendar and Gmail.
  - **Complexity:** Medium (14 nodes)

- **[2669-ollama-chat-ai.json](workflows/2669-ollama-chat-ai.json)**
  - **Description:** This flow processes chat messages using local language models in Ollama and returns structured responses in JSON.
  - **Complexity:** Medium (14 nodes)

- **[2969-chatbot_line.json](workflows/2969-chatbot_line.json)**
  - **Description:** This workflow configures a chatbot in LINE that displays a loading animation when receiving a message and uses an AI agent with CBT to respond to users. If the message is not text, it sends a warning.
  - **Complexity:** Medium (14 nodes)

- **[3066-generar_fondo_grafico.json](workflows/3066-generar_fondo_grafico.json)**
  - **Description:** This flow uses Midjourney, GPT-4o-mini and Canvas API to generate a graphic wallpaper with an emotional copy. First, GPT-4o-mini generates text based on the provided theme and scenario, then Midjourney creates an image according to the description, and finally Canvas designs the final composition with text and visual elements.
  - **Complexity:** Medium (14 nodes)

- **[3183-ollama-chat-flow.json](workflows/3183-ollama-chat-flow.json)**
  - **Description:** This flow processes chat messages using Ollama's Llama 3.2 model through a basic LLM chain to generate structured responses in JSON format.
  - **Complexity:** Medium (14 nodes)

- **[3230-gemini-bounding-box.json](workflows/3230-gemini-bounding-box.json)**
  - **Description:** This flow uses the Gemini 2.0 API to detect objects in images and draw custom bounding boxes.
  - **Complexity:** Medium (14 nodes)

- **[0987-line-chatbot-llm-extraction.json](workflows/0987-line-chatbot-llm-extraction.json)**
  - **Description:** This automated flow uses a self-hosted LLM model (Mistral Nemo) to extract personal information from messages received in LINE, analyzing and structuring the response according to a predefined JSON schema.
  - **Complexity:** Medium (13 nodes)

- **[2811-gmail-auto-label.json](workflows/2811-gmail-auto-label.json)**
  - **Description:** Automates email categorization in Gmail using OpenAI to label messages based on existing ones or create new labels if necessary.
  - **Complexity:** Medium (13 nodes)

- **[2888-automatizacion-ticket.json](workflows/2888-automatizacion-ticket.json)**
  - **Description:** This flow automates the generation and triage of tickets. It uses Gmail to extract support messages, OpenAI to triage and tag each ticket, and Linear.app to create an issue based on the results.
  - **Complexity:** Medium (13 nodes)

- **[2989-motion-illustration.json](workflows/2989-motion-illustration.json)**
  - **Description:** This flow generates an animated illustration using Midjourney and Kling API. First it creates an image with Midjourney, then waits and processes the status to generate a video with Kling, finally returns the video URL without watermark.
  - **Complexity:** Medium (13 nodes)

- **[3007-travel-agent-couchbase-vector.json](workflows/3007-travel-agent-couchbase-vector.json)**
  - **Description:** This flow uses Google Gemini 2.0 Flash and OpenAI to create a travel planning agent with vector search capability in Couchbase, allowing searching and storing points of interest.
  - **Complexity:** Medium (13 nodes)

- **[3043-three-view-to-video.json](workflows/3043-three-view-to-video.json)**
  - **Description:** Converts three-dimensional orthogonal projections into dynamic animated video using GPT-4o and Kling to generate images and videos.
  - **Complexity:** Medium (13 nodes)

- **[0544-n8n-daily-ai-news.json](workflows/0544-n8n-daily-ai-news.json)**
  - **Description:** This automatic flow searches for artificial intelligence (AI) related articles using the NewsAPI and GNews APIs, merges them and uses GPT-4 to summarize and translate them into traditional Chinese while keeping technical terms in English.
  - **Complexity:** Medium (12 nodes)

- **[0901-linear-bugs-classifier.json](workflows/0901-linear-bugs-classifier.json)**
  - **Description:** This automated flow classifies new bugs in Linear using OpenAI GPT-4 to determine the correct team based on a predefined list of responsibilities and updates or notifies if a suitable destination is not found.
  - **Complexity:** Medium (12 nodes)

- **[1022-gmail-ai-auto-responder.json](workflows/1022-gmail-ai-auto-responder.json)**
  - **Description:** This automatic flow analyzes incoming emails and decides whether to respond using OpenAI artificial intelligence, creating drafts in Gmail for conversations.
  - **Complexity:** Medium (12 nodes)

- **[1029-seo-onpage-audit.json](workflows/1029-seo-onpage-audit.json)**
  - **Description:** This flow analyzes the on-page SEO of a landing page using GPT models to generate detailed reports.
  - **Complexity:** Medium (12 nodes)

- **[1031-open-meteo-ai-chat.json](workflows/1031-open-meteo-ai-chat.json)**
  - **Description:** This automatic flow uses Open-Meteo API functions (Tools) with ChatGPT to determine the exact location of a city requested by the user and, subsequently, use those coordinates to generate a detailed weather forecast.
  - **Complexity:** Medium (12 nodes)

- **[1032-ai-agents-http-tool.json](workflows/1032-ai-agents-http-tool.json)**
  - **Description:** This flow allows users to request activities or information via an AI query, using integrated HTTP tools that simplify API calls.
  - **Complexity:** Medium (12 nodes)

- **[1136-linear-ai-classification.json](workflows/1136-linear-ai-classification.json)**
  - **Description:** This flow automatic classifies bug tickets in Linear using AI (OpenAI) and assigns the responsible team based on their work areas. The ticket is analyzed, the AI determines the appropriate team and it is updated in Linear.
  - **Complexity:** Medium (12 nodes)

- **[1208-pdf-image-extractor.json](workflows/1208-pdf-image-extractor.json)**
  - **Description:** This automatic flow extracts images from PDFs, analyzes each image with the GPT-4o model and generates a text document integrating the results.
  - **Complexity:** Medium (12 nodes)

- **[1234-twitter-ai-influencer-schedule.json](workflows/1234-twitter-ai-influencer-schedule.json)**
  - **Description:** This automated flow generates and publishes tweets periodically using artificial intelligence to maintain a specific influencer style.
  - **Complexity:** Medium (12 nodes)

- **[1431-ai-chat-with-any-data-workflow.json](workflows/1431-ai-chat-with-any-data-workflow.json)**
  - **Description:** This flow allows chatbot using OpenAI/GPT with artificial intelligence and APIs.
  - **Complexity:** Medium (12 nodes)

- **[1476-integrating-ai-with-open-meteo-api.json](workflows/1476-integrating-ai-with-open-meteo-api.json)**
  - **Description:** This flow allows chatbot using OpenAI/GPT, Webhook with artificial intelligence through webhooks and APIs.
  - **Complexity:** Medium (12 nodes)

- **[2613-airflow-dag-monitor.json](workflows/2613-airflow-dag-monitor.json)**
  - **Description:** This automatic flow allows initiating a DAG execution in Airflow via an API and checking its status to take action as needed.
  - **Complexity:** Medium (12 nodes)

- **[0394-manejador-errores.json](workflows/0394-manejador-errores.json)**
  - **Description:** This flow checks if a workflow is active and does not have an error handler configured. If so, it updates its settings by assigning the ID of the default error handler via an API call.
  - **Complexity:** Medium (11 nodes)

- **[0443-comparativo-llm-pdf.json](workflows/0443-comparativo-llm-pdf.json)**
  - **Description:** This automated flow allows testing and comparing the ability of Gemini 2.0 Flash and Claude 3.5 Sonnet models to extract information directly from PDFs using predefined credentials.
  - **Complexity:** Medium (11 nodes)

- **[0505-openai-image-generation-edit.json](workflows/0505-openai-image-generation-edit.json)**
  - **Description:** This workflow allows generating an initial image using the OpenAI API, converting it to binary format and then editing it by adding elements such as horns using the same API.
  - **Complexity:** Medium (11 nodes)

- **[0917-email-drafting-fastmail-openai.json](workflows/0917-email-drafting-fastmail-openai.json)**
  - **Description:** This automatic flow analyzes unread emails from an IMAP mailbox via the Fastmail API and generates responses using models such as GPT-4, saving drafts to a specific folder.
  - **Complexity:** Medium (11 nodes)

- **[0925-cv-screening-openai.json](workflows/0925-cv-screening-openai.json)**
  - **Description:** This automated flow analyzes PDF resumes using the OpenAI API, creating structured evaluations with a percentage score and detailed summaries.
  - **Complexity:** Medium (11 nodes)

- **[1003-ia-output-parser.json](workflows/1003-ia-output-parser.json)**
  - **Description:** This flow forces AIs to use a specific output format via structured or self-fixing parsers, ensuring organized and validated responses.
  - **Complexity:** Medium (11 nodes)

- **[2801-email-reply-draft.json](workflows/2801-email-reply-draft.json)**
  - **Description:** This automatic flow uses OpenAI to generate email responses and saves them to the Fastmail drafts folder.
  - **Complexity:** Medium (11 nodes)

- **[2921-ai-agent-charts-generator.json](workflows/2921-ai-agent-charts-generator.json)**
  - **Description:** This flow allows an artificial intelligence agent to generate personalized charts in conversations using OpenAI Structured Output to define Chart.js and Quickchart.io chart configurations.
  - **Complexity:** Medium (11 nodes)

- **[0516-email-classification-ai.json](workflows/0516-email-classification-ai.json)**
  - **Description:** This flow processes emails, classifies them into specific categories using models of OpenAI and extracts relevant information about the candidates.
  - **Complexity:** Medium (10 nodes)

- **[0772-generador_3d_figurine.json](workflows/0772-generador_3d_figurine.json)**
  - **Description:** This flow uses Midjourney to generate base images and GPT-4o to create orthogonal views of 3D characters.
  - **Complexity:** Medium (10 nodes)

- **[1427-ai-agent-with-ollama-for-current-weather-and-wiki.json](workflows/1427-ai-agent-with-ollama-for-current-weather-and-wiki.json)**
  - **Description:** This flow allows chatbot with artificial intelligence and APIs.
  - **Complexity:** Medium (10 nodes)

- **[1501-text-automations-using-apple-shortcuts-1.json](workflows/1501-text-automations-using-apple-shortcuts-1.json)**
  - **Description:** This flow allows automation, summary using OpenAI/GPT, Webhook with artificial intelligence through webhooks and APIs.
  - **Complexity:** Medium (10 nodes)

- **[2657-calendar-agent.json](workflows/2657-calendar-agent.json)**
  - **Description:** This automatic flow allows a chatbot to interact with the user's calendar, creating individual or attendee events, obtaining schedules and deleting them. The Google Calendar conversational agent uses GPT models to handle requests.
  - **Complexity:** Medium (10 nodes)

- **[2994-gemini-video-analysis.json](workflows/2994-gemini-video-analysis.json)**
  - **Description:** This flow analyzes videos using the Gemini AI API. It downloads a video, uploads it to Google servers and generates a detailed description using the Gemini-2.0-flash-exp model.
  - **Complexity:** Medium (10 nodes)

- **[3199-text_automation.json](workflows/3199-text_automation.json)**
  - **Description:** Flow to automate text translation and editing tasks using Apple Shortcuts and OpenAI. It analyzes the type of request, performs the corresponding action with GPT-4 Mini and responds to the Shortcut.
  - **Complexity:** Medium (10 nodes)

- **[3332-text-automations-shortcuts.json](workflows/3332-text-automations-shortcuts.json)**
  - **Description:** This flow uses Apple Shortcuts to send texts to a webhook and use OpenAI to perform different tasks such as translating, correcting grammar or adjusting text length.
  - **Complexity:** Medium (10 nodes)

- **[1458-discord-ai-powered-bot.json](workflows/1458-discord-ai-powered-bot.json)**
  - **Description:** This flow allows chatbot, summary using OpenAI/GPT, Webhook with artificial intelligence through webhooks and APIs.
  - **Complexity:** Medium (9 nodes)

- **[2595-line-chatbot-ai.json](workflows/2595-line-chatbot-ai.json)**
  - **Description:** This automatic flow allows a LINE chatbot to maintain conversations using Groq and Llama3, sending incoming messages as requests to the AI to generate responses.
  - **Complexity:** Medium (9 nodes)

- **[0664-tts-openai.json](workflows/0664-tts-openai.json)**
  - **Description:** This flow allows text-to-speech conversion using the OpenAI speech synthesis service.
  - **Complexity:** Medium (8 nodes)

- **[0909-openai-tts-manual.json](workflows/0909-openai-tts-manual.json)**
  - **Description:** This flow allows converting text to speech using the OpenAI API with a manual process.
  - **Complexity:** Medium (8 nodes)

- **[1508-use-openrouter-in-n8n-versions-_178.json](workflows/1508-use-openrouter-in-n8n-versions-_178.json)**
  - **Description:** This flow allows chatbot using OpenAI/GPT, Webhook with artificial intelligence through webhooks and APIs.
  - **Complexity:** Medium (8 nodes)

- **[2959-centroid_calculator.json](workflows/2959-centroid_calculator.json)**
  - **Description:** This flow calculates the centroid of a set of vectors. It receives a GET request with an array of vectors, validates that they are consistent and calculates their centroid.
  - **Complexity:** Medium (8 nodes)

- **[0956-html-generator.json](workflows/0956-html-generator.json)**
  - **Description:** This flow uses OpenAI Structured Output along with n8n to dynamically generate HTML pages based on user requests, using a predefined JSON schema and Tailwind CSS as a framework.
  - **Complexity:** Medium (7 nodes)

- **[0981-html-generator.json](workflows/0981-html-generator.json)**
  - **Description:** This automatic flow allows dynamically generating complete HTML pages based on user requests using the structure defined by OpenAI. The process sends the user's text to the GPT-4o-mini API with a specific JSON schema, then converts that JSON response to complete HTML.
  - **Complexity:** Medium (7 nodes)

- **[1055-line-chatbot-search.json](workflows/1055-line-chatbot-search.json)**
  - **Description:** This automatic flow allows a LINE chatbot to search the web when the user makes queries, using tools such as SearchAPI.io and LLM models such as OpenAI.
  - **Complexity:** Medium (7 nodes)

- **[3169-siri_ai_agent.json](workflows/3169-siri_ai_agent.json)**
  - **Description:** Flow that uses Siri to activate an OpenAI agent via Apple Shortcuts, processing voice commands and generating responses.
  - **Complexity:** Medium (7 nodes)

- **[3177-email-to-line-summarizer.json](workflows/3177-email-to-line-summarizer.json)**
  - **Description:** This flow automates reading emails, summarizes them with artificial intelligence and sends them to the LINE messenger.
  - **Complexity:** Medium (7 nodes)

- **[0157-line-syncro-timer-sync.json](workflows/0157-line-syncro-timer-sync.json)**
  - **Description:** This automatic flow synchronizes time entries in Syncro from a webhook that receives information about phone calls from a chatbot.
  - **Complexity:** Medium (6 nodes)

- **[0334-line-chatbot-memory.json](workflows/0334-line-chatbot-memory.json)**
  - **Description:** This automated flow processes chat messages in LINE using contextualized memory to maintain a significant history and calls the specified assistant to generate responses.
  - **Complexity:** Medium (6 nodes)

- **[0367-tweets-publicador.json](workflows/0367-tweets-publicador.json)**
  - **Description:** This automatic flow extracts and publishes the latest Tweets stored in a Google sheet called 'Tweets' every 6 hours.
  - **Complexity:** Medium (6 nodes)

- **[0378-elevenlabs-text-to-speech.json](workflows/0378-elevenlabs-text-to-speech.json)**
  - **Description:** This flow verifies input parameters and uses the ElevenLabs API to generate voice responses from the provided text.
  - **Complexity:** Medium (6 nodes)

- **[0447-perplexity-ai-chat.json](workflows/0447-perplexity-ai-chat.json)**
  - **Description:** This automated flow sends a request to the Perplexity AI API using the provided key, including parameters such as prompt and domains for filtering.
  - **Complexity:** Medium (6 nodes)

- **[0513-email-tracking-pixel.json](workflows/0513-email-tracking-pixel.json)**
  - **Description:** This automated flow allows detecting when an email is opened by sending a transparent PNG image via webhook, capturing parameters such as userId to identify the sender.
  - **Complexity:** Medium (6 nodes)

- **[0691-openai-image-gen.json](workflows/0691-openai-image-gen.json)**
  - **Description:** This automatic flow uses the OpenAI ImageGen v1 API to edit images and generate a new version based on the provided prompt.
  - **Complexity:** Medium (6 nodes)

- **[1013-openai-image-generation.json](workflows/1013-openai-image-generation.json)**
  - **Description:** This automatic flow allows generating multiple images using the GPT-4 model for OpenAI images via its API.
  - **Complexity:** Medium (6 nodes)

- **[1018-elevenlabs-tts-api.json](workflows/1018-elevenlabs-tts-api.json)**
  - **Description:** This automatic flow allows generating audio from text using the Elevenlabs API via webhooks, first verifying that the 'voice_id' and 'text' parameters are correctly provided.
  - **Complexity:** Medium (6 nodes)

- **[1057-analisis-feedback-ia.json](workflows/1057-analisis-feedback-ia.json)**
  - **Description:** This flow processes customer comments, analyzes feedback with artificial intelligence to obtain a summary, suggestions for improvement and ideas for social posts, and then sends the results by email to the team's address.
  - **Complexity:** Medium (6 nodes)

- **[1086-perplexity-api-query.json](workflows/1086-perplexity-api-query.json)**
  - **Description:** This automatic flow queries the Perplexity AI API using the Sonar model with a system prompt and a user request, and then cleanly processes the response.
  - **Complexity:** Medium (6 nodes)

- **[0012-typeform-feedback-route.json](workflows/0012-typeform-feedback-route.json)**
  - **Description:** This flow analyzes Typeform form responses and classifies them into Google spreadsheets based on whether the numerical value 'usefulness' is greater than or equal to 3.
  - **Complexity:** Medium (5 nodes)

- **[0364-documentacion-n8n-automatica.json](workflows/0364-documentacion-n8n-automatica.json)**
  - **Description:** This automatic flow allows users to generate documentation for their n8n workflows using the OpenAI API.
  - **Complexity:** Medium (5 nodes)

- **[0442-transform-image-to-lego-line.json](workflows/0442-transform-image-to-lego-line.json)**
  - **Description:** This automatic flow allows receiving an image via a LINE webhook, analyzing it with GPT-4O-MINI to create the appropriate prompt in DALL-E 3, generating the allegorical image as if it were made of LEGO and finally sending this new image to the user via Line.
  - **Complexity:** Medium (5 nodes)

- **[0489-line-n8n-assistant.json](workflows/0489-line-n8n-assistant.json)**
  - **Description:** This flow implements an AI assistant in n8n that responds to LINE messages using GPT models and MCP tools.
  - **Complexity:** Medium (5 nodes)

- **[0515-auto-iniciar-flujos-n8n.json](workflows/0515-auto-iniciar-flujos-n8n.json)**
  - **Description:** This flow allows manually starting two execution instances in n8n via the trigger. The description explains that these flows do not start automatically after import, unless they have the 'Auto start' tag and are configured to auto-deploy.
  - **Complexity:** Medium (5 nodes)

- **[0675-clockify-proyecto-entrada-tiempo.json](workflows/0675-clockify-proyecto-entrada-tiempo.json)**
  - **Description:** This automatic flow creates a project in Clockify with specific details and then adds a time entry using that project, maintaining context consistency.
  - **Complexity:** Medium (5 nodes)

- **[0845-openai-image-generator.json](workflows/0845-openai-image-generator.json)**
  - **Description:** This workflow allows generating images using the OpenAI API based on inputs provided via forms.
  - **Complexity:** Medium (5 nodes)

- **[0892-ollama-n8n-chat.json](workflows/0892-ollama-n8n-chat.json)**
  - **Description:** This flow allows interacting with local language models (managed by Ollama) through a chat interface.
  - **Complexity:** Medium (5 nodes)

- **[1068-openai-tts-audio-generation.json](workflows/1068-openai-tts-audio-generation.json)**
  - **Description:** This flow allows generating audio from text using the OpenAI Text-to-Speech (TTS) API. A webhook is configured to receive POST requests that include the text to be converted.
  - **Complexity:** Medium (5 nodes)

- **[1429-ai-agent-chat.json](workflows/1429-ai-agent-chat.json)**
  - **Description:** This flow allows chatbot using OpenAI/GPT, Webhook with artificial intelligence through webhooks and APIs.
  - **Complexity:** Medium (5 nodes)

- **[3185-transform-image-to-lego.json](workflows/3185-transform-image-to-lego.json)**
  - **Description:** This flow transforms an image received via LINE into a LEGO style using the DALL-E API.
  - **Complexity:** Medium (5 nodes)

- **[0045-google-books-automation.json](workflows/0045-google-books-automation.json)**
  - **Description:** This automatic flow obtains information from a specific volume and adds it to a bookshelf in the Google Books API via a sequence of calls with OAuth2 authentication.
  - **Complexity:** Low (4 nodes)

- **[0178-thehive-case-management.json](workflows/0178-thehive-case-management.json)**
  - **Description:** This automatic flow allows creating, updating and obtaining a case in TheHive via a sequence of connected steps.
  - **Complexity:** Low (4 nodes)

- **[0289-mistral-cadena-hf.json](workflows/0289-mistral-cadena-hf.json)**
  - **Description:** This flow uses a basic LLM chain connected to Hugging Face's Mistral-7B-Instruct-v0.1 model along with generation options such as temperature and penalty.
  - **Complexity:** Low (4 nodes)

- **[0181-cortex-abuse-detector.json](workflows/0181-cortex-abuse-detector.json)**
  - **Description:** This flow analyzes a URL using the Abuse Finder node in Cortex, and then obtains job details using the returned ID.
  - **Complexity:** Low (3 nodes)

- **[0534-speech-recognition-wit-ai.json](workflows/0534-speech-recognition-wit-ai.json)**
  - **Description:** This automated flow uses the Read Binary File node to read a WAV file at the specified path and sends it to the Wit.ai API via an HTTP POST request for processing.
  - **Complexity:** Low (2 nodes)

- **[1192-json-array-splitter.json](workflows/1192-json-array-splitter.json)**
  - **Description:** This workflow takes an initial input containing a JSON list and expands it into multiple flows, each with an individual array element for further processing.
  - **Complexity:** Low (2 nodes)

- **[0184-thehive-event-monitor.json](workflows/0184-thehive-event-monitor.json)**
  - **Description:** This flow monitors all events in the TheHive system and triggers an action when one occurs.
  - **Complexity:** Low (1 nodes)

- **[1516-Legal_Assistant.json](workflows/1516-Legal_Assistant.json)**
  - **Description:** Answers legal queries using a vector knowledge base.
  - **Complexity:** Medium (8 nodes)

- **[1526-Advanced_RAG_System.json](workflows/1526-Advanced_RAG_System.json)**
  - **Description:** RAG (Retrieval-Augmented Generation) system that loads documents, extracts metadata, splits them into articles, stores them in Qdrant and answers queries using an AI agent.
  - **Complexity:** High (25 nodes)

- **[1527-SQL_Assistant.json](workflows/1527-SQL_Assistant.json)**
  - **Description:** SQL assistant that converts natural language to SQL queries for an online store database and responds in natural language.
  - **Complexity:** Low (4 nodes)

- **[1539-Cohere_Reranker_RAG.json](workflows/1539-Cohere_Reranker_RAG.json)**
  - **Description:** RAG system that uses Cohere to re-rank search results from a Qdrant vector database.
  - **Complexity:** High (17 nodes)

- **[1540-AI_Model_Router.json](workflows/1540-AI_Model_Router.json)**
  - **Description:** Language model selector that classifies user queries and directs them to the appropriate AI model (calendar, internet search, legal queries).
  - **Complexity:** High (18 nodes)

- **[1545-Slack_RAG_Agent.json](workflows/1545-Slack_RAG_Agent.json)**
  - **Description:** RAG agent for Slack that loads documents, processes them, stores them in a vector database and responds to Slack queries.
  - **Complexity:** High (20 nodes)


### Web Scraping and Data Extraction

- **[0990-google-trends-automatizacion.json](workflows/0990-google-trends-automatizacion.json)**
  - **Description:** This automatic flow analyzes Google Trends results, filters by minimum traffic and maximum results, then extracts information from related articles by scraping with Jina.ai. If the conditions are met (e.g., adequate traffic and new terms), it saves the information to a Google sheet for tracking.
  - **Complexity:** High (26 nodes)

- **[2802-webhook-relay.json](workflows/2802-webhook-relay.json)**
  - **Description:** This automatic flow uses webhook.site to receive and store requests, then processes them and forwards them to a local address via n8n. An authentication token and a key are used to synchronize the state between executions.
  - **Complexity:** High (18 nodes)

- **[2885-reddit-business-opportunities.json](workflows/2885-reddit-business-opportunities.json)**
  - **Description:** This flow automates the extraction and analysis of Reddit posts relevant to business opportunities, applying filters and generating summaries with LLM.
  - **Complexity:** High (17 nodes)

- **[2591-chatbot-jina-scraper.json](workflows/2591-chatbot-jina-scraper.json)**
  - **Description:** This automatic flow allows a chatbot to integrate real-time web scraping via Jina.ai to respond to queries intelligently.
  - **Complexity:** Medium (9 nodes)

- **[0490-mediamarkt-deals.json](workflows/0490-mediamarkt-deals.json)**
  - **Description:** This automatic flow processes and sends product offers classified by category via web scraping.
  - **Complexity:** Medium (8 nodes)

- **[2627-whatsapp-webhook-echo.json](workflows/2627-whatsapp-webhook-echo.json)**
  - **Description:** This workflow verifies a webhook with a GET request and responds to POST Requests containing user messages, sending these messages as responses in WhatsApp.
  - **Complexity:** Medium (8 nodes)

- **[0680-firecrawl-markdown-extractor.json](workflows/0680-firecrawl-markdown-extractor.json)**
  - **Description:** This automatic flow uses FireCrawl to perform web scraping from a provided URL, formatting the result as markdown text to facilitate its use in applications and agents.
  - **Complexity:** Low (4 nodes)

- **[2529-firecrawl-tool.json](workflows/2529-firecrawl-tool.json)**
  - **Description:** This flow allows any user to send URLs to get responses from the Firecrawl API and keep them as editable fields in the workflow context.
  - **Complexity:** Low (4 nodes)

- **[2975-conversion-rate-optimizer.json](workflows/2975-conversion-rate-optimizer.json)**
  - **Description:** This flow automates conversion rate optimization by analyzing a landing page via scraping and using an AI agent to perform critical analysis and propose specific improvements.
  - **Complexity:** Low (4 nodes)


### Autonomous Agents and Dynamic Logic

- **[1392-deep_researcher.json](workflows/1392-deep_researcher.json)**
  - **Description:** Deep research agent with AI.
  - **Complexity:** High (85 nodes)

- **[1423-bot_handoff.json](workflows/1423-bot_handoff.json)**
  - **Description:** Transfers a bot conversation to a human agent.
  - **Complexity:** High (39 nodes)

- **[1393-ai_phone_agent_retell.json](workflows/1393-ai_phone_agent_retell.json)**
  - **Description:** AI phone agent that uses Retell.
  - **Complexity:** High (36 nodes)

- **[1274-proxmox-ai-agent.json](workflows/1274-proxmox-ai-agent.json)**
  - **Description:** Agent that automates tasks on Proxmox servers with AI.
  - **Complexity:** High (35 nodes)

- **[3065-chat-voice-agent-RAG.json](workflows/3065-chat-voice-agent-RAG.json)**
  - **Description:** This flow integrates a chatbot, voice agent and telephony with Voiceflow, Google Calendar and RAG to manage appointments, perform searches and rely on Qdrant vectors.
  - **Complexity:** High (34 nodes)

- **[3201-whatsapp-ai-sales-agent.json](workflows/3201-whatsapp-ai-sales-agent.json)**
  - **Description:** This automatic flow uses WhatsApp to receive user messages and respond to them via an AI agent integrated with a vectorized knowledge base. It includes downloading a PDF catalog, processing and storing it in a vector store, as well as handling unsupported message types.
  - **Complexity:** High (28 nodes)

- **[1160-customer-lead-ai-processing.json](workflows/1160-customer-lead-ai-processing.json)**
  - **Description:** This automatic flow processes contact requests using an AI agent, analyzing notes to determine if they are valid and generating professional emails when required.
  - **Complexity:** High (27 nodes)

- **[1546-Multiagent_Email_Calendar.json](workflows/1546-Multiagent_Email_Calendar.json)**
  - **Description:** n8n multi-agent that manages emails and calendars, with support for voice transcription and different language models.
  - **Complexity:** High (23 nodes)

- **[1547-Multiagent_Email_Calendar_Advanced.json](workflows/1547-Multiagent_Email_Calendar_Advanced.json)**
  - **Description:** n8n multi-agent that manages emails and calendars, with support for voice transcription and different language models.
  - **Complexity:** High (23 nodes)

- **[1517-Legal_Assistant_Bot.json](workflows/1517-Legal_Assistant_Bot.json)**
  - **Description:** Lawyer assistant that uses Telegram, transcribes audio, and uses sub-agents for email, calendar, contacts and legislation.
  - **Complexity:** High (19 nodes)

- **[2644-openai-form-dynamic.json](workflows/2644-openai-form-dynamic.json)**
  - **Description:** This automatic flow allows a chatbot to dynamically generate forms based on user responses and the analysis of a previous open question, thus avoiding asking redundant information.
  - **Complexity:** High (19 nodes)

- **[0009-multi-agente-ia.json](workflows/0009-multi-agente-ia.json)**
  - **Description:** This flow allows maintaining a multi-route conversation with multiple AI agents based on defined models and configurations, combining their responses and incorporating memory for tracking.
  - **Complexity:** High (18 nodes)

- **[1520-Voice_Assistant_Transcriber.json](workflows/1520-Voice_Assistant_Transcriber.json)**
  - **Description:** Voice assistant that transcribes audio, analyzes user sentiment and intent, and saves information to Google Sheets.
  - **Complexity:** High (17 nodes)

- **[1542-n8n_Flowise_RAG.json](workflows/1542-n8n_Flowise_RAG.json)**
  - **Description:** n8n flow that integrates with Flowise for a RAG system, allowing document loading and query answering via Telegram.
  - **Complexity:** High (17 nodes)

- **[3074-erp-chatbot-odoo.json](workflows/3074-erp-chatbot-odoo.json)**
  - **Description:** This automatic flow allows a chatbot contextualized with window memory to retrieve and summarize Odoo business opportunities, using calculation tools and conversational agents to improve user assistance.
  - **Complexity:** High (16 nodes)

- **[2690-blockchain_dex_insights_agent.json](workflows/2690-blockchain_dex_insights_agent.json)**
  - **Description:** This automatic flow acts as an insights agent for DEX blockchain, using different analysis tools and the DexScreener API to provide real-time information on tokens and trading pairs.
  - **Complexity:** Medium (15 nodes)

- **[1162-typeform-klicktipp-quiz.json](workflows/1162-typeform-klicktipp-quiz.json)**
  - **Description:** This automated flow processes Typeform form responses to create contacts in KlickTipp and assign dynamic tags based on the responses.
  - **Complexity:** Medium (14 nodes)

- **[1557-Voice_Assistant_MCP.json](workflows/1557-Voice_Assistant_MCP.json)**
  - **Description:** Voice assistant that uses a webhook trigger, transcribes audio, and uses MCP agents to manage Gmail, Calendar and Contacts.
  - **Complexity:** High (13 nodes)

- **[3315-coin_market_cap_crypto_agent.json](workflows/3315-coin_market_cap_crypto_agent.json)**
  - **Description:** Decryptive agent flow that uses CoinMarketCap API to analyze and provide cryptocurrency information through an integrated natural language analysis system with memory.
  - **Complexity:** Medium (13 nodes)

- **[0398-agente-ia-herramientas.json](workflows/0398-agente-ia-herramientas.json)**
  - **Description:** This demo flow allows an AI agent to interact with web tools and APIs to provide activities or information via messages.
  - **Complexity:** Medium (12 nodes)

- **[0281-llm-chain-ai-agent.json](workflows/0281-llm-chain-ai-agent.json)**
  - **Description:** This flow executes an LLM chain to generate responses and uses an AI agent with tools like Wikipedia to improve searches in conversations.
  - **Complexity:** Medium (10 nodes)

- **[0921-n8n-flujo-langchain.json](workflows/0921-n8n-flujo-langchain.json)**
  - **Description:** This flow allows executing two types of interactions: one to obtain responses with custom LLM chains and another that uses a chat agent integrated with WikipediaQueryRun as a tool.
  - **Complexity:** Medium (10 nodes)

- **[0203-n8n-fecha-dinamica.json](workflows/0203-n8n-fecha-dinamica.json)**
  - **Description:** This flow uses Luxon expressions to dynamically calculate and format dates in n8n.
  - **Complexity:** Medium (9 nodes)

- **[1054-outlook-ai-response.json](workflows/1054-outlook-ai-response.json)**
  - **Description:** This automatic flow connects a Microsoft Outlook account to filter and process specific incoming emails (in this case 'sales@yourcompany.com'), using an AI agent that responds with a professional, concise and modern style based on predefined examples.
  - **Complexity:** Medium (9 nodes)

- **[2614-custom-ai-agent-memory.json](workflows/2614-custom-ai-agent-memory.json)**
  - **Description:** This flow configures a custom AI agent with specific characteristics such as personality, conversation topics and response styles in Chinese. Interaction is done through the chat integrated in n8n.
  - **Complexity:** Medium (9 nodes)

- **[0456-keywords-analysis.json](workflows/0456-keywords-analysis.json)**
  - **Description:** This automatic flow processes keywords from a Google sheet, analyzes them to determine if they contain IT software names via an AI agent and updates the sheet with the results.
  - **Complexity:** Medium (8 nodes)

- **[1528-Flowise_Chat_Agent.json](workflows/1528-Flowise_Chat_Agent.json)**
  - **Description:** Flowise conversational agent that uses OpenAI, Redis for memory, content moderation and an information retrieval tool (Qdrant).
  - **Complexity:** Medium (8 nodes)

- **[1534-Phone_Assistant.json](workflows/1534-Phone_Assistant.json)**
  - **Description:** Phone assistant that interacts with a webhook, extracts call information, and uses MCP agents to manage calendars and Gmail.
  - **Complexity:** Medium (8 nodes)

- **[1535-MCP_Calendar_Flow.json](workflows/1535-MCP_Calendar_Flow.json)**
  - **Description:** MCP flow that manages calendar events (create, delete, get, update, check availability) via an MCP trigger.
  - **Complexity:** Medium (8 nodes)

- **[1553-Multiagente_MCP.json](workflows/1553-Multiagente_MCP.json)**
  - **Description:** n8n multi-agent that manages emails, calendars and contacts via MCP.
  - **Complexity:** Medium (8 nodes)

- **[1556-Asistente_de_Voz.json](workflows/1556-Asistente_de_Voz.json)**
  - **Description:** Voice assistant that interacts with a webhook, saves data to Google Sheets and sends WhatsApp messages.
  - **Complexity:** Medium (8 nodes)

- **[2543-openrouter-llm-agent.json](workflows/2543-openrouter-llm-agent.json)**
  - **Description:** This flow configures an AI agent that uses different language models via OpenRouter and maintains conversational memory for chats.
  - **Complexity:** Medium (8 nodes)

- **[0373-nasa-api-credentials.json](workflows/0373-nasa-api-credentials.json)**
  - **Description:** This flow uses a form to dynamically enter the NASA API key, which is then used in the connection node with NASA via expressions.
  - **Complexity:** Medium (7 nodes)

- **[1543-MCP_Calendar_Flow.json](workflows/1543-MCP_Calendar_Flow.json)**
  - **Description:** MCP flow that manages calendar events (create, delete, get, update, check availability) via an MCP trigger.
  - **Complexity:** Medium (7 nodes)

- **[0471-line-chatbot-ssh.json](workflows/0471-line-chatbot-ssh.json)**
  - **Description:** This automatic flow allows a LINE chatbot to interactively request help with SSH commands and execute them on a VPS, using tools such as ReAct Agent and the n8n-nodes-base extension.
  - **Complexity:** Medium (6 nodes)

- **[0739-peekalink-verificacion.json](workflows/0739-peekalink-verificacion.json)**
  - **Description:** This flow checks if a service is available by querying a specific URL and using logical conditions.
  - **Complexity:** Medium (6 nodes)

- **[1521-MCP_Calendar_Voice.json](workflows/1521-MCP_Calendar_Voice.json)**
  - **Description:** MCP flow that manages calendar events (create, delete, get, update) via an MCP trigger.
  - **Complexity:** Medium (6 nodes)

- **[1523-MCP_Gmail_Voice.json](workflows/1523-MCP_Gmail_Voice.json)**
  - **Description:** MCP flow that manages emails (send, reply, create drafts, get, delete) via an MCP trigger.
  - **Complexity:** Medium (6 nodes)

- **[1536-MCP_Gmail_Flow.json](workflows/1536-MCP_Gmail_Flow.json)**
  - **Description:** MCP flow that manages emails (send, reply, create drafts, get, delete) via an MCP trigger.
  - **Complexity:** Medium (6 nodes)

- **[1544-MultiLLM_Customer_Agent.json](workflows/1544-MultiLLM_Customer_Agent.json)**
  - **Description:** Customer service assistant with multi-LLM functionality that offers AI and automation services, and can schedule meetings.
  - **Complexity:** Medium (6 nodes)

- **[1550-MCP_Calendar_Flow.json](workflows/1550-MCP_Calendar_Flow.json)**
  - **Description:** MCP flow that manages calendar events (create, delete, get, update, check availability) via an MCP trigger.
  - **Complexity:** Medium (6 nodes)

- **[1552-MCP_Gmail_Flow.json](workflows/1552-MCP_Gmail_Flow.json)**
  - **Description:** MCP flow that manages emails (send, reply, create drafts, get, delete) via an MCP trigger.
  - **Complexity:** Medium (6 nodes)

- **[1558-MCP_Calendar_Voice_Flow.json](workflows/1558-MCP_Calendar_Voice_Flow.json)**
  - **Description:** MCP flow that manages calendar events (create, delete, get, update) via an MCP trigger.
  - **Complexity:** Medium (6 nodes)

- **[1560-MCP_Gmail_Voice_Flow.json](workflows/1560-MCP_Gmail_Voice_Flow.json)**
  - **Description:** MCP flow that manages emails (send, reply, create drafts, get, delete) via an MCP trigger.
  - **Complexity:** Medium (6 nodes)

- **[1538-n8n_Flowise_Integration.json](workflows/1538-n8n_Flowise_Integration.json)**
  - **Description:** n8n flow that integrates with Flowise to send Telegram messages.
  - **Complexity:** Low (3 nodes)

- **[1522-MCP_Contacts_Voice.json](workflows/1522-MCP_Contacts_Voice.json)**
  - **Description:** MCP flow that adds contacts to Google Sheets via an MCP trigger.
  - **Complexity:** Low (2 nodes)

- **[1537-Hair_Salon_Agent.json](workflows/1537-Hair_Salon_Agent.json)**
  - **Description:** Hair salon agent that uses tools to answer queries and manage conversation flow.
  - **Complexity:** Low (2 nodes)

- **[1541-Flowise_RAG_Agent.json](workflows/1541-Flowise_RAG_Agent.json)**
  - **Description:** Flowise agent flow that uses a RAG system to answer legal queries.
  - **Complexity:** Low (2 nodes)

- **[1551-MCP_Contacts_Flow.json](workflows/1551-MCP_Contacts_Flow.json)**
  - **Description:** MCP flow that adds contacts to Google Sheets via an MCP trigger.
  - **Complexity:** Low (2 nodes)

- **[1559-MCP_Contacts_Voice_Flow.json](workflows/1559-MCP_Contacts_Voice_Flow.json)**
  - **Description:** MCP flow that adds contacts to Google Sheets via an MCP trigger.
  - **Complexity:** Low (2 nodes)

### Other / Miscellaneous

- **[1524-n8n_Tips_and_Tricks.json](workflows/1524-n8n_Tips_and_Tricks.json)**
  - **Description:** Demonstrates 5 n8n tricks, including human approval, error handling, current date and time, test data and user interface.
  - **Complexity:** High (20 nodes)

- **[1269-api-schema-extractor.json](workflows/1269-api-schema-extractor.json)**
  - **Description:** Extracts and documents an API schema.
  - **Complexity:** High (88 nodes)

- **[2936-api_schema_extractor.json](workflows/2936-api_schema_extractor.json)**
  - **Description:** Extracts API schemas by identifying and processing technical documentation online to generate a custom schema.
  - **Complexity:** High (88 nodes)

- **[1263-meeting-reminder-bot.json](workflows/1263-meeting-reminder-bot.json)**
  - **Description:** Bot that sends meeting reminders via messaging.
  - **Complexity:** High (61 nodes)

- **[1399-startups-funding-monitor.json](workflows/1399-startups-funding-monitor.json)**
  - **Description:** Monitors startup funding rounds.
  - **Complexity:** High (51 nodes)

- **[2540-agricultural-anomaly-detection.json](workflows/2540-agricultural-anomaly-detection.json)**
  - **Description:** This flow configures the centers of each agricultural cluster and sets thresholds for anomaly detection in crop images.
  - **Complexity:** High (48 nodes)

- **[2700-cloudflare_kv_management.json](workflows/2700-cloudflare_kv_management.json)**
  - **Description:** This flow manages Cloudflare KV Storage operations such as listing, creating, deleting and renaming namespaces, as well as performing specific actions with key-value pairs.
  - **Complexity:** High (47 nodes)

- **[1277-baserow-llm-updates.json](workflows/1277-baserow-llm-updates.json)**
  - **Description:** Performs updates in Baserow using a language model.
  - **Complexity:** High (45 nodes)

- **[0864-n8n_leaderboard_stats.json](workflows/0864-n8n_leaderboard_stats.json)**
  - **Description:** This automated flow analyzes n8n user metrics to generate a detailed and formatted Markdown report, including ranking of most popular workflows and creator statistics.
  - **Complexity:** High (43 nodes)

- **[1415-survey_insights_qdrant.json](workflows/1415-survey_insights_qdrant.json)**
  - **Description:** Analyzes survey responses and saves vectors to Qdrant.
  - **Complexity:** High (42 nodes)

- **[1261-ai-interview-flow.json](workflows/1261-ai-interview-flow.json)**
  - **Description:** Automates interviews using AI-generated questions.
  - **Complexity:** High (40 nodes)

- **[2963-spotify-sync-playlist.json](workflows/2963-spotify-sync-playlist.json)**
  - **Description:** This flow synchronizes songs marked as favorites on Spotify with a specific playlist. It automatically adds new songs that are in your liked songs but not in the playlist and removes those that have been removed from your liked songs.
  - **Complexity:** High (40 nodes)

- **[1414-spot-discrimination-analysis.json](workflows/1414-spot-discrimination-analysis.json)**
  - **Description:** Detects discrimination in texts using AI.
  - **Complexity:** High (38 nodes)

- **[0922-trustpilot-customer-insights.json](workflows/0922-trustpilot-customer-insights.json)**
  - **Description:** This automatic flow extracts information from customer reviews on TrustPilot using Qdrant to store vectors and LLMs to generate insights into overall sentiment and identify recurring themes.
  - **Complexity:** High (37 nodes)

- **[1420-graphic-design-flow.json](workflows/1420-graphic-design-flow.json)**
  - **Description:** Automates basic graphic design tasks.
  - **Complexity:** High (37 nodes)

- **[3070-spotify-archiver.json](workflows/3070-spotify-archiver.json)**
  - **Description:** This automatic flow archives monthly Spotify favorite songs to a Google spreadsheet and classifies tracks into playlists using an AI model.
  - **Complexity:** High (37 nodes)

- **[0861-line-chatbot-memory.json](workflows/0861-line-chatbot-memory.json)**
  - **Description:** This automatic flow allows a LINE chatbot to maintain a contextualized conversation with its users by using memory via the service's REST API.
  - **Complexity:** High (35 nodes)

- **[2905-analyze-email-headers.json](workflows/2905-analyze-email-headers.json)**
  - **Description:** This flow analyzes email headers to detect IP addresses and fraud. It extracts IPs from 'received' headers and queries their reputation using the IP Quality Score API, also verifies SPF, DKIM and DMARC authentication.
  - **Complexity:** High (35 nodes)

- **[3122-Proxmox-AI-Agent.json](workflows/3122-Proxmox-AI-Agent.json)**
  - **Description:** This automatic flow manages tasks in Proxmox using n8n and generative AI. It analyzes commands, validates inputs, generates API commands and executes them.
  - **Complexity:** High (35 nodes)

- **[3135-docker-immich-deploy.json](workflows/3135-docker-immich-deploy.json)**
  - **Description:** This flow configures and manages Docker environments for the Immich application, including deploy, start, stop, suspend, mount/unmount disks and manage users and ACLs. It uses SSH and Webhooks to interact with the server.
  - **Complexity:** High (35 nodes)

- **[0926-docker_n8n_api_workflow.json](workflows/0926-docker_n8n_api_workflow.json)**
  - **Description:** This automatic flow handles the creation and management of Docker containers via an API with basic authentication.
  - **Complexity:** High (34 nodes)

- **[1417-bitrix-chatbot-rag.json](workflows/1417-bitrix-chatbot-rag.json)**
  - **Description:** Chatbot in Bitrix with RAG search.
  - **Complexity:** High (34 nodes)

- **[0904-line-chatbot-memory.json](workflows/0904-line-chatbot-memory.json)**
  - **Description:** This automated flow allows a LINE chatbot to maintain a contextualized conversation by using persistent memory.
  - **Complexity:** High (33 nodes)

- **[0928-n8n_workflow_stats.json](workflows/0928-n8n_workflow_stats.json)**
  - **Description:** This automatic flow allows users to obtain detailed statistics about n8n workflows, including node information, global, tags, webhooks and more. It uses advanced JS functions such as JMESPath for efficient processing.
  - **Complexity:** High (33 nodes)

- **[3008-minio-deploy.json](workflows/3008-minio-deploy.json)**
  - **Description:** This flow automates the deployment and management of Docker containers for MinIO on a server with WHMCS/WISECP. It handles operations such as creating, starting, stopping, suspending, mounting/unmounting disks and configuring ACLs, as well as integration with Nginx for access.
  - **Complexity:** High (33 nodes)

- **[1267-email_subscription_workflow.json](workflows/1267-email_subscription_workflow.json)**
  - **Description:** Manages email subscriptions automatically.
  - **Complexity:** High (32 nodes)

- **[2532-pdf-digital-sign-service.json](workflows/2532-pdf-digital-sign-service.json)**
  - **Description:** This automatic flow allows the generation of digital keys and certificates to sign PDF documents.
  - **Complexity:** High (32 nodes)

- **[2647-whatsapp-ai-chatbot.json](workflows/2647-whatsapp-ai-chatbot.json)**
  - **Description:** This automated flow allows a chatbot on WhatsApp to intelligently analyze and respond to different types of messages: text, voice, images and PDFs.
  - **Complexity:** High (32 nodes)

- **[0823-ai-monitoring-slack.json](workflows/0823-ai-monitoring-slack.json)**
  - **Description:** This automated flow monitors articles of interest in real time using multiple RSS sources, classifies their relevance with AI and generates formatted summaries to facilitate efficient management.
  - **Complexity:** High (31 nodes)

- **[0962-email-ai-assistant.json](workflows/0962-email-ai-assistant.json)**
  - **Description:** This automatic flow analyzes incoming emails using AI to summarize them and generate responses, allowing human reviews when necessary.
  - **Complexity:** High (31 nodes)

- **[1394-yoga-line-bot.json](workflows/1394-yoga-line-bot.json)**
  - **Description:** LINE bot that sends yoga routines.
  - **Complexity:** High (31 nodes)

- **[1273-service_now_search_bot.json](workflows/1273-service_now_search_bot.json)**
  - **Description:** Bot that searches for information in ServiceNow.
  - **Complexity:** High (29 nodes)

- **[2787-contabo-backups.json](workflows/2787-contabo-backups.json)**
  - **Description:** This automatic flow schedules daily snapshots of instances in Contabo, checking and deleting if a snapshot already exists before creating a new one.
  - **Complexity:** High (29 nodes)

- **[2980-reddit-pr-report.json](workflows/2980-reddit-pr-report.json)**
  - **Description:** This flow automates the identification of trending stories by analyzing Reddit discussions and their subsequent analysis with LLM to generate strategic PR reports.
  - **Complexity:** High (29 nodes)

- **[0784-ai-meeting-tool.json](workflows/0784-ai-meeting-tool.json)**
  - **Description:** This automatic flow allows an AI assistant to manage meeting transcripts and perform automated actions such as creating events in Google Calendar for follow-up.
  - **Complexity:** High (28 nodes)

- **[3054-business-canvas-generator.json](workflows/3054-business-canvas-generator.json)**
  - **Description:** Flow that generates a Business Model Canvas from chat inputs, using LLM for each section and transforming the results into HTML.
  - **Complexity:** High (28 nodes)

- **[3283-sync-email-templates.json](workflows/3283-sync-email-templates.json)**
  - **Description:** This flow synchronizes email templates between Dartagnan and Braze. It retrieves templates from Dartagnan, compares them with existing ones in Braze and updates or creates new ones as appropriate.
  - **Complexity:** High (28 nodes)

- **[3128-gmail-mcp-server.json](workflows/3128-gmail-mcp-server.json)**
  - **Description:** This flow configures an MCP server to interact with Gmail, allowing operations such as searching, deleting, marking as read, adding or removing labels and more.
  - **Complexity:** High (27 nodes)

- **[2781-spotify-mqtt-controller.json](workflows/2781-spotify-mqtt-controller.json)**
  - **Description:** This flow handles MQTT commands from a remote button to control Spotify, including volume and playback, as well as playing favorite lists.
  - **Complexity:** High (26 nodes)

- **[3127-email-ai-responder.json](workflows/3127-email-ai-responder.json)**
  - **Description:** This flow automates responding to emails using DeepSeek R1 to summarize and send professional replies.
  - **Complexity:** High (26 nodes)

- **[3210-google_maps_email_scraper.json](workflows/3210-google_maps_email_scraper.json)**
  - **Description:** This flow extracts and processes business emails from Google Maps using a list of queries. It searches for URLs related to initial searches, filters irrelevant ones, scrapes resulting pages to find email addresses, removes duplicates and imports results to a Google spreadsheet.
  - **Complexity:** High (26 nodes)

- **[0867-linea_inventario_agendador.json](workflows/0867-linea_inventario_agendador.json)**
  - **Description:** This automatic flow allows an n8n chatbot to schedule meetings by checking Google Calendar availability and generating 30-minute time slots between business hours from Monday to Friday.
  - **Complexity:** High (25 nodes)

- **[3217-appointment-scheduling-flow.json](workflows/3217-appointment-scheduling-flow.json)**
  - **Description:** This flow automates professional appointment management using interactive forms and human approval. It receives requests, classifies inquiries with AI, validates terms, schedules dates/times, notifies the user and manages approved or rejected appointments.
  - **Complexity:** High (25 nodes)

- **[1268-automatizacion_becas_ai.json](workflows/1268-automatizacion_becas_ai.json)**
  - **Description:** Automates the scholarship application process using AI.
  - **Complexity:** High (24 nodes)

- **[1278-chatbot-citas.json](workflows/1278-chatbot-citas.json)**
  - **Description:** Chatbot for automatically scheduling appointments.
  - **Complexity:** High (24 nodes)

- **[3094-flujo-get-scaleway-servers.json](workflows/3094-flujo-get-scaleway-servers.json)**
  - **Description:** This flow automates obtaining and filtering server information in Scaleway, including instances and baremetal, allowing searching by tags, name, public IP or zone.
  - **Complexity:** High (24 nodes)

- **[0711-phishing-analysis-n8n.json](workflows/0711-phishing-analysis-n8n.json)**
  - **Description:** This automatic flow analyzes indicators of compromise in emails, extracts URLs and scans them with VirusTotal and URLScan.io to detect potential phishing threats.
  - **Complexity:** High (23 nodes)

- **[2655-_Generate_AI-Ready_llms.txt_Files_from_Screaming_Frog.json](workflows/2655-_Generate_AI-Ready_llms.txt_Files_from_Screaming_Frog.json)**
  - **Description:** Transforms a CSV exported from Screaming Frog into an optimized `llms.txt` file with titles, URLs and indexability information, facilitating crawling and classification by language models.
  - **Complexity:** High (23 nodes)

- **[2846-news-email-digest.json](workflows/2846-news-email-digest.json)**
  - **Description:** Flow that collects, processes and selects articles from Calcalist and Mako RSS to send a daily email summary formatted with the most relevant ones for executives.
  - **Complexity:** High (23 nodes)

- **[2915-mcp-google-calendar.json](workflows/2915-mcp-google-calendar.json)**
  - **Description:** This flow configures an MCP server integrated with Google Calendar to perform calendar operations such as creating, updating and deleting events using specific tools.
  - **Complexity:** High (23 nodes)

- **[3255-flujo-independiente.json](workflows/3255-flujo-independiente.json)**
  - **Description:** This flow implements an independent process that initiates a secondary execution via a webhook and resumes it in the main context.
  - **Complexity:** High (23 nodes)

- **[1422-analyze_reddit_posts_business_opportunities.json](workflows/1422-analyze_reddit_posts_business_opportunities.json)**
  - **Description:** Analyzes Reddit posts for business opportunities.
  - **Complexity:** High (22 nodes)

- **[3261-bbc_podcast_workflow.json](workflows/3261-bbc_podcast_workflow.json)**
  - **Description:** This flow extracts and classifies BBC news, generates a podcast script using LLM and sends them to Hugging Face for audio conversion.
  - **Complexity:** High (22 nodes)

- **[3288-follow_up_meetings.json](workflows/3288-follow_up_meetings.json)**
  - **Description:** This automatic flow monitors past sales appointments to detect if follow-up messages have been sent and suggests new available appointments to the user to schedule a new meeting if necessary.
  - **Complexity:** High (22 nodes)

- **[3336-credenciales-transfer-n8n.json](workflows/3336-credenciales-transfer-n8n.json)**
  - **Description:** Flow to transfer credentials between n8n instances. It allows selecting a target instance and a source credential, then exports, processes and sends the credential to the destination.
  - **Complexity:** High (22 nodes)

- **[1421-automated-seo-audit-report.json](workflows/1421-automated-seo-audit-report.json)**
  - **Description:** Generates SEO audit reports automatically.
  - **Complexity:** High (21 nodes)

- **[2580-multiple-local-llm-testing.json](workflows/2580-multiple-local-llm-testing.json)**
  - **Description:** This automatic flow allows testing multiple local LLM models in LM Studio via HTTP requests and detailed response analysis.
  - **Complexity:** High (21 nodes)

- **[2637-line-bitrix-task-integration.json](workflows/2637-line-bitrix-task-integration.json)**
  - **Description:** This automatic flow allows a LINE chatbot to maintain a contextualized conversation and update user information in Bitrix24 to manage tasks.
  - **Complexity:** High (21 nodes)

- **[2654-comparador-multiples-modelos.json](workflows/2654-comparador-multiples-modelos.json)**
  - **Description:** This flow allows comparing multiple language model responses while maintaining separate memory per model.
  - **Complexity:** High (21 nodes)

- **[2671-performance-testing-multi-llm.json](workflows/2671-performance-testing-multi-llm.json)**
  - **Description:** This automatic flow allows multiple tests of local language models (LLM) via the LM Studio server, analyzing metrics such as readability score and average word length for each response.
  - **Complexity:** High (21 nodes)

- **[2868-sustentabilidad-news.json](workflows/2868-sustentabilidad-news.json)**
  - **Description:** This automatic flow extracts and classifies EU news, identifying if it is related to sustainability, and sends a summary by email.
  - **Complexity:** High (21 nodes)

- **[3005-chinese-translator-line.json](workflows/3005-chinese-translator-line.json)**
  - **Description:** This flow translates LINE messages using OpenRouter.ai to obtain Chinese characters, pinyin and English translation.
  - **Complexity:** High (21 nodes)

- **[0006-airtable-hn-job-scraping.json](workflows/0006-airtable-hn-job-scraping.json)**
  - **Description:** This automatic flow allows extracting and structuring job offers published in 'Ask HN: Who is hiring' on Hacker News using the Algolia API.
  - **Complexity:** High (20 nodes)

- **[0960-gitea-backup-workflow.json](workflows/0960-gitea-backup-workflow.json)**
  - **Description:** This automatic flow checks and saves n8n workflows to a Git repository hosted on Gitea by comparing changes and updates.
  - **Complexity:** High (20 nodes)

- **[2561-inteligente-busqueda-web.json](workflows/2561-inteligente-busqueda-web.json)**
  - **Description:** This flow uses multiple thought chains and LLM models to generate optimal queries, perform web searches and implement a semantic re-ranking system that evaluates results and provides structured relevant information.
  - **Complexity:** High (20 nodes)

- **[2903-extraer_y_decodificar_noticias_google.json](workflows/2903-extraer_y_decodificar_noticias_google.json)**
  - **Description:** This flow extracts and decodes Google News URLs from its RSS feed, cleaning links to obtain clear and accessible articles.
  - **Complexity:** High (20 nodes)

- **[2932-bluesky-threads.json](workflows/2932-bluesky-threads.json)**
  - **Description:** This flow creates threads in Bluesky using authentication and HTTP requests to publish initial posts and nested replies with a waiting and looping scheme.
  - **Complexity:** High (20 nodes)

- **[0828-podcast-consciencia-ai.json](workflows/0828-podcast-consciencia-ai.json)**
  - **Description:** This flow analyzes podcasts on the philosophy of mind, extracts key information and performs Wikipedia searches to generate improved summaries.
  - **Complexity:** High (19 nodes)

- **[1081-retry-on-fail-known-error.json](workflows/1081-retry-on-fail-known-error.json)**
  - **Description:** This flow implements a retry mechanism for an action, but avoids retries in case of specific known errors such as 'could not be found'.
  - **Complexity:** High (19 nodes)

- **[1143-seo-serp-analysis.json](workflows/1143-seo-serp-analysis.json)**
  - **Description:** This automatic flow searches for and processes Google search results for SEO analysis.
  - **Complexity:** High (19 nodes)

- **[1403-web-security-audit.json](workflows/1403-web-security-audit.json)**
  - **Description:** Performs automated web security audits.
  - **Complexity:** High (19 nodes)

- **[2687-flujo-verificacion-voz-correo.json](workflows/2687-flujo-verificacion-voz-correo.json)**
  - **Description:** This automatic flow sends voice messages for verification and then verifies the code via email.
  - **Complexity:** High (19 nodes)

- **[2792-flujo-imagen-ai.json](workflows/2792-flujo-imagen-ai.json)**
  - **Description:** Flow that generates AI images based on prompts and styles selected by the user, using the Hugging Face API. The user can choose between different visual styles such as cyberpunk or neon to create advanced visual compositions.
  - **Complexity:** High (19 nodes)

- **[1006-rag-stock-analysis.json](workflows/1006-rag-stock-analysis.json)**
  - **Description:** This flow analyzes profitability reports using RAG to generate a detailed report in markdown format on trends and differences.
  - **Complexity:** High (18 nodes)

- **[1149-google-docs-image-replace.json](workflows/1149-google-docs-image-replace.json)**
  - **Description:** Google Docs automation with dynamic image replacement.
  - **Complexity:** High (18 nodes)

- **[1157-n8n-multi-workflow.json](workflows/1157-n8n-multi-workflow.json)**
  - **Description:** This automatic flow allows executing multiple sub-jobs in parallel and tracking their status until all are completed.
  - **Complexity:** High (18 nodes)

- **[2539-lands-knn-classification.json](workflows/2539-lands-knn-classification.json)**
  - **Description:** This workflow uses KNN with satellite images to classify landscape types using Voyage AI model embeddings and Qdrant queries. When there are ties, it increases the number of neighbors until a clear majority is found.
  - **Complexity:** High (18 nodes)

- **[2663-n8n-image-editor-flux-fill.json](workflows/2663-n8n-image-editor-flux-fill.json)**
  - **Description:** This flow allows processing images via inpainting with the FLUX Fill tool, integrating user interactions in a visual editor based on Konva.js.
  - **Complexity:** High (18 nodes)

- **[2683-podcast_workflow.json](workflows/2683-podcast_workflow.json)**
  - **Description:** This automatic flow processes a podcast episode by splitting its transcript, summarizing it and generating related questions and topics, then formatting the information in HTML and sending it via Gmail.
  - **Complexity:** High (18 nodes)

- **[3017-knn_land_classifier.json](workflows/3017-knn_land_classifier.json)**
  - **Description:** This flow uses a KNN classifier to determine the class of an image based on its vector embedding. First, it obtains the image embedding via the Voyage AI API, then queries Qdrant with this embedding to find the nearest neighbors and applies majority voting to resolve conflicts.
  - **Complexity:** High (18 nodes)

- **[3104-flux-image-edit.json](workflows/3104-flux-image-edit.json)**
  - **Description:** This flow handles an image fill request using the FLUX API. First it receives an image and a mask via a webhook, then processes the image with the AI model to generate an edited version based on a prompt provided by the user.
  - **Complexity:** High (18 nodes)

- **[3260-fact-checking_workflow.json](workflows/3260-fact-checking_workflow.json)**
  - **Description:** This flow automates fact-checking and text analysis. It separates a text into sentences, uses LLM to mark statements as correct or incorrect, and produces a report with identified inaccuracies.
  - **Complexity:** High (18 nodes)

- **[0822-email-approval-ia.json](workflows/0822-email-approval-ia.json)**
  - **Description:** This flow automates the processing of incoming emails, generates summaries and responses using RAG and AI, requires Yes/No approval before sending them.
  - **Complexity:** High (17 nodes)

- **[0873-opensea-marketplace-agent.json](workflows/0873-opensea-marketplace-agent.json)**
  - **Description:** This automatic flow allows a chatbot to interact with the OpenSea API to obtain information about listados, offers and NFT orders in different collections and identifiers.
  - **Complexity:** High (17 nodes)

- **[1137-pdf-qa-vector-store.json](workflows/1137-pdf-qa-vector-store.json)**
  - **Description:** This flow processes chat messages to answer questions about a PDF using the vector stored in Qdrant.
  - **Complexity:** High (17 nodes)

- **[2573-workflow-ai-investigacion.json](workflows/2573-workflow-ai-investigacion.json)**
  - **Description:** This flow uses LLMs to generate search queries, process results and synthesize a complete research report.
  - **Complexity:** High (17 nodes)

- **[2620-n8n-workflow-clone.json](workflows/2620-n8n-workflow-clone.json)**
  - **Description:** This flow allows cloning workflows between different n8n instances via the API, processing batches to optimize performance.
  - **Complexity:** High (17 nodes)
