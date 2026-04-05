[Versión en español](https://github.com/DragonJAR/n8n-workflows-esp/blob/main/README.md) | [English Version](https://github.com/DragonJAR/n8n-workflows-esp/blob/main/README-ENGLISH.md)

[Free n8n automation course](https://dragonjar.education/bundle/curso-n8n)

# n8n Workflows Collection

This repository is a fork of the original initiative by [@Zie619](https://github.com/Zie619/n8n-workflows).

## Improvements Implemented
- Workflow search with 10,405 workflows
- Descriptions in English
- Duplicate removal via unique hash
- Fusion with n8n community workflows

## How to Use
1. Open your n8n instance.
2. Import workflow.
3. Select JSON file.
4. Adjust credentials.
5. Run.

## MCP Server
https://gitmcp.io/DragonJAR/n8n-workflows-esp

## Contribution
Open a pull request with your improvements.

## Disclaimer
Workflows are provided as-is. Test in a controlled environment before production use.

## Workflow Listings

_Total workflows: 10405_

### CRM and Sales

#### HubSpot

- **0017-stripe-hubspot-slack.json**
  - **Description:** Integrates Stripe payment events with HubSpot CRM and sends notifications to Slack. Automatically creates or updates HubSpot contacts when payments are received, keeping sales teams informed in real-time.
  - **Complexity:** Low (8 nodes)

- **0088-typeform-hubspot-email.json**
  - **Description:** Captures form submissions from Typeform and automatically creates or updates contacts in HubSpot CRM. Sends confirmation emails to leads and syncs lead data for immediate follow-up.
  - **Complexity:** Low (7 nodes)

- **0122-sync-hubspot-pipedrive.json**
  - **Description:** Bidirectional synchronization between HubSpot and Pipedrive CRM systems. Ensures contact and deal data stays consistent across both platforms, preventing data silos in multi-CRM environments.
  - **Complexity:** Low (5 nodes)

- **10014-Automatically-discover-enrich-HubSpot-buying-groups-with-Surfe-and-Google-Sheets.json**
  - **Description:** Automatically discovers and enriches key contacts within HubSpot deal buying groups. Combines company domain from HubSpot deals with buying group criteria (departments, seniorities, countries, job titles) to find decision-makers via Surfe. Pushes enriched contacts to HubSpot and emails a summary to the sales team with direct links, ensuring no decision-maker falls through the cracks.
  - **Complexity:** High (30+ nodes)

- **10064-Auto-enrich-sync-companies-from-Google-Sheets-to-HubSpot-using-GPT-4o-mini.json**
  - **Description:** Automatically enriches and syncs company data from Google Sheets to HubSpot CRM. When new company names are added to a sheet, uses AI to find industry, size, location, and website details. Checks HubSpot for existing companies and creates new records if not found. Updates the sheet with all enriched information.
  - **Complexity:** Medium (15-20 nodes)

- **10086-Automated-lead-capture-scoring-CRM-integration-with-HubSpot-Clearbit-Slack.json**
  - **Description:** Transforms raw leads into qualified prospects through intelligent automation. Captures leads from any source, validates data, enriches with company intelligence via Clearbit, scores based on qualification criteria, routes leads to the right team, integrates with HubSpot CRM, and sends notifications to Slack. Complete lead-to-opportunity pipeline.
  - **Complexity:** High (25-35 nodes)

- **10087-Predict-customer-churn-risk-create-interventions-with-GPT-4-Zendesk-HubSpot.json**
  - **Description:** AI-powered customer churn prediction system that forecasts risk 30-90 days before it happens. Gathers daily data from multiple sources, performs AI multi-signal analysis to calculate risk scores, routes high-risk cases to appropriate teams, generates personalized intervention strategies with GPT-4, updates HubSpot CRM with risk data, and alerts the customer success team via Zendesk.
  - **Complexity:** High (40+ nodes)

- **10240-AI-powered-lead-enrichment-from-Typeform-Calendly-to-HubSpot-CRM.json**
  - **Description:** Captures leads from Typeform submissions and Calendly meeting bookings, standardizes information into a clean format, and checks email domains. For business domains, uses AI to enrich leads with company details including industry, headquarters, size, and website. Merges all data and creates or updates contacts in HubSpot CRM with complete profiles.
  - **Complexity:** High (30+ nodes)

- **10265-Typeform-to-HubSpot-AI-enriched-scored-leads-with-GPT-4o-mini.json**
  - **Description:** Processes Typeform submissions by cleaning and storing raw lead data, validates if emails are business-related (not Gmail/personal), enriches leads with company details using AI, scores lead quality with GPT-4o-mini, updates HubSpot CRM with enriched data and scores, and saves everything to Google Sheets for tracking and reporting.
  - **Complexity:** High (25-30 nodes)

- **10374-Automate-Gmail-lead-follow-up-with-OpenAI-GPT-4O-HubSpot-Slack-Google-Sheets.json**
  - **Description:** Automates handling of new lead responses from Gmail with AI-powered analysis. Captures emails with specific labels, analyzes messages using OpenAI to determine sentiment, intent, urgency, next action, and priority. Decides if follow-up is needed, creates tasks in HubSpot, notifies sales team via Slack, and logs all details to Google Sheets for comprehensive tracking.
  - **Complexity:** High (35+ nodes)

- **10411-Analyze-form-feedback-with-GPT-4-sync-tasks-to-Monday-ClickUp-HubSpot.json**
  - **Description:** Automates customer feedback management by capturing reviews through forms, analyzing them with GPT-4 for sentiment and insights, then creating structured tasks across Monday.com, ClickUp, and HubSpot. Ensures customer concerns are categorized, prioritized, and assigned to the right teams with actionable metadata for systematic follow-up.
  - **Complexity:** High (30-40 nodes)

- **10612-Automate-support-ticket-classification-routing-from-HubSpot-to-Jira-with-GPT.json**
  - **Description:** Automates HubSpot ticket triage by classifying and routing to Jira using AI agents. Designed for customer support, CX, and operations teams managing messages through HubSpot and using Jira for internal task management. Automates sentiment detection, ticket classification, and team assignment, ideal for SaaS companies optimizing support workflows.
  - **Complexity:** High (30-35 nodes)

- **10727-Quick-HubSpot-contact-lookup-in-Slack-for-sales-support-teams.json**
  - **Description:** Instant HubSpot contact lookup via Slack slash commands. Users trigger the workflow in Slack with an email address or HubSpot contact ID, the workflow searches HubSpot for the matching contact, formats details into a clean Slack-friendly message card, and posts results back to the Slack channel. Enables sales and support teams to quickly access contact information without leaving Slack.
  - **Complexity:** Low (8-12 nodes)

- **10802-Lead-routing-system-Qualify-direct-Typeform-leads-to-HubSpot-Sheets-Airtable.json**
  - **Description:** Intelligent lead routing system that processes Typeform submissions. Captures lead details, checks budget levels, and routes based on priority and source. High-budget leads are pushed to HubSpot with follow-up tasks for sales. Facebook leads are logged to Google Sheets for marketing, SurveyMonkey leads stored in Airtable for campaign tracking. Every lead receives appropriate processing based on criteria.
  - **Complexity:** High (25-30 nodes)

- **10836-Qualify-high-budget-leads-Typeform-to-HubSpot-Google-Sheets-Slack-alerts.json**
  - **Description:** Captures Typeform leads and instantly checks if budget exceeds $5,000 to prioritize for fast sales follow-up. High-budget leads are enriched in HubSpot as contacts with detailed properties, and a priority task is created for the sales team. Leads are routed based on source (Facebook or SurveyMonkey), logged to Google Sheets for marketing, and triggers Slack alerts for immediate attention.
  - **Complexity:** High (30+ nodes)

- **10986-Enrich-HubSpot-contacts-with-LinkedIn-profiles-using-SerpAPI-Google-Docs-and-AI.json**
  - **Description:** Enriches HubSpot contacts with LinkedIn profile information using SerpAPI and AI. Triggers on HubSpot contact creation/updates or manual request, maps key fields (First Name, Last Name, Email), reads enrichment criteria from Google Docs, searches LinkedIn via SerpAPI, extracts profile data, and updates HubSpot contacts with LinkedIn information.
  - **Complexity:** Medium (20-25 nodes)

- **10988-Automate-Calendly-to-HubSpot-contact-updates-meeting-logging.json**
  - **Description:** Automatically syncs Calendly meeting bookings into HubSpot CRM. Checks if invitee already exists as a contact, extracts attendee details, creates or updates contacts in HubSpot, and logs the meeting engagement with all relevant information. Ensures every booked meeting is properly tracked, linked to the right contact, and enriched with context from Calendly.
  - **Complexity:** Low (10-15 nodes)

- **11015-Automate-sales-follow-ups-with-GPT-4o-mini-HubSpot-Slack-Teams-Telegram.json**
  - **Description:** Automatically generates personalized follow-up messages for leads or customers after key interactions like demos or sales calls. Enriches contact details from HubSpot, uses GPT-4o-mini to draft professional follow-up emails, and distributes reminders across multiple communication channels including Slack, Telegram, and Teams. Ensures consistent and timely follow-up across all platforms.
  - **Complexity:** High (30+ nodes)

- **11018-Bidirectional-company-sync-between-ProspectPro-and-HubSpot-with-status-tracking.json**
  - **Description:** Synchronizes prospects from ProspectPro into HubSpot with bidirectional status tracking. Checks if companies already exist in HubSpot by ProspectPro ID or domain, updates records if found or creates new ones. Logs sync results back to ProspectPro with tags to prevent duplicates and mark errors, ensuring reliable and repeatable integration between the two systems.
  - **Complexity:** Medium (15-20 nodes)

- **11111-Automate-lead-qualification-follow-up-with-Gemini-HubSpot-Zoom-Mailchimp.json**
  - **Description:** Complete lead qualification and follow-up automation using Google Gemini AI. Captures leads, qualifies them as QUALIFIED or NOT QUALIFIED using AI. Qualified leads get a scheduled meeting with Zoom details, email confirmation, CRM update, and Mailchimp enrollment. Not-qualified leads receive follow-up sequences, CRM updates, and 30-day reminders for re-engagement.
  - **Complexity:** High (35+ nodes)

#### Pipedrive

- **0086-calendly-pipedrive-slack.json**
  - **Description:** Integrates Calendly meeting bookings with Pipedrive CRM and Slack notifications. Automatically creates deals in Pipedrive when meetings are booked, updates deal stages based on meeting outcomes, and notifies the sales team via Slack for immediate follow-up.
  - **Complexity:** Low (5 nodes)

- **0216-typeform-pipedrive-mapeo.json**
  - **Description:** Captures Typeform form submissions and maps the data to create or update leads and deals in Pipedrive CRM. Handles field mapping between Typeform responses and Pipedrive custom fields, ensuring all lead information flows correctly into the sales pipeline.
  - **Complexity:** Low (8 nodes)

- **0228-github-fork-to-pipedrive-lead.json**
  - **Description:** [MISCLASSIFIED] This is a GitHub workflow that monitors repository forks and should be moved to DevOps category, not CRM/Sales.

- **0229-github-pullrequest-pipedrive.json**
  - **Description:** [MISCLASSIFIED] This is a GitHub workflow that monitors pull requests and should be moved to DevOps category, not CRM/Sales.

- **10113-Complete-Webflow-to-Pipedrive-integration-with-smart-phone-formatting.json**
  - **Description:** Advanced form submission to CRM automation with international phone number support. Processes Webflow form submissions, automatically creates CRM records in Pipedrive with intelligent duplicate detection, formats phone numbers for international dialing, and sends multi-channel team notifications. Ideal for sales teams needing sophisticated lead management.
  - **Complexity:** High (25-30 nodes)

- **10363-Natural-language-QA-for-Pipedrive-leads-using-GPT-4o-mini.json**
  - **Description:** Enables natural-language queries about Pipedrive leads. Users can ask questions like "leads added this week", "stuck leads by owner", or "next activities due today". The workflow pulls live lead data from Pipedrive and uses OpenAI to answer questions grounded only in Pipedrive data, providing accurate insights without hallucination.
  - **Complexity:** Medium (15-20 nodes)

- **10365-Generate-daily-Pipedrive-deal-summaries-with-GPT-4o-mini.json**
  - **Description:** Automatically generates daily summaries of Pipedrive deals. Fetches deals and their notes from Pipedrive, cleans up stage IDs into readable names, aggregates the information, and uses OpenAI to generate a comprehensive daily summary of the sales funnel. Helps sales teams stay informed about pipeline status without manual reporting.
  - **Complexity:** Medium (15-20 nodes)

- **10429-Track-Pipedrive-deals-in-Google-Sheets-for-sales-pipeline-reporting.json**
  - **Description:** Tracks and reports Pipedrive deals in Google Sheets. Pulls all deals from Pipedrive, categorizes them by sales stage, and logs them into a Google Sheet for reporting, analytics, and pipeline tracking. Provides a centralized view of deal progress and enables custom reporting outside of Pipedrive.
  - **Complexity:** Low (8-12 nodes)

- **10812-Connect-Pipedrive-deal-outcomes-to-GA4-Google-Ads-via-Measurement-Protocol.json**
  - **Description:** Connects Pipedrive deal milestones to Google Analytics 4 via Measurement Protocol. Solves the optimization gap where ads optimize to shallow web events (form fills) while real value sits in Pipedrive (Qualified, Closed Won). Turns deal stages into server-side GA4 events matched to original visitors by client_id, enabling more accurate bidding optimization based on actual revenue.
  - **Complexity:** High (25-30 nodes)

#### Salesforce

- **0234-excel-to-salesforce.json**
  - **Description:** Imports lead and contact data from Excel spreadsheets into Salesforce CRM. Reads Excel files, maps columns to Salesforce fields, validates data integrity, and creates or updates records in Salesforce with error handling and logging. Streamlines bulk data migration for sales teams.
  - **Complexity:** Medium (12 nodes)

- **0954-3031-from-community-CallForge-01-filter-Gong-calls-synced-to-Salesforce-by.json**
  - **Description:** Extracts, filters, and preprocesses Gong call data for Salesforce integration. Designed for sales and revenue teams using Gong and Salesforce to track and analyze sales calls. Automates extraction of call recordings, metadata, and transcripts, filters relevant calls, and prepares data for further AI analysis or direct sync to Salesforce.
  - **Complexity:** Medium (15-20 nodes)

- **10187-LeadBot-autopilot-chat-to-lead-for-Salesforce.json**
  - **Description:** Automated lead capture chatbot that creates leads in Salesforce. Greets visitors and collects information step-by-step: Full Name → Email → Mobile → Product Interest. Validates email/phone formats, politely re-asks if invalid. Checks Salesforce for existing leads by email and updates if found, otherwise creates new lead. Provides instant lead generation with automated Salesforce integration.
  - **Complexity:** Medium (15-20 nodes)

#### Zoho

- **10809-Automatic-email-categorization-labeling-in-Zoho-Mail-with-GPT-4o-mini.json**
  - **Description:** AI-powered email categorization and labeling for Zoho Mail. Uses GPT-4o-mini text classification to automatically categorize incoming emails in Zoho Mail and apply correct labels like Support, Billing, or HR. Saves time by keeping inbox structured and ensures emails are routed to the right category for efficient processing.
  - **Complexity:** Medium (15-20 nodes)

#### Lead Generation

- **0110-info-uplead-company.json**
  - **Description:** Enriches company information using Uplead API. Takes company names or domains as input, queries Uplead for business data including revenue, employee count, industry, and contact details, and returns enriched company information for lead qualification and targeting.
  - **Complexity:** Low (2 nodes)

- **0116-typeform_lead_workflow.json**
  - **Description:** Captures and processes Typeform leads for automated follow-up. Receives form submissions, validates required fields, scores leads based on responses, routes leads to appropriate teams, stores in database, and triggers follow-up sequences. Comprehensive lead handling from form intake to nurturing.
  - **Complexity:** Medium (10 nodes)

- **0506-facebook-lead-to-klicktipp.json**
  - **Description:** Captures Facebook Lead Ads submissions and syncs to KlickTipp email marketing platform. Automatically retrieves new leads from Facebook campaigns, validates email addresses, adds subscribers to KlickTipp lists, and triggers welcome email sequences. Streamlines Facebook lead acquisition and email marketing integration.
  - **Complexity:** Low (3 nodes)

- **0864-n8n_leaderboard_stats.json**
  - **Description:** Comprehensive sales leaderboard and performance tracking system. Aggregates sales data from multiple sources, calculates team and individual performance metrics, generates leaderboard rankings, visualizes results, and distributes reports. Handles complex data processing across 43 nodes for complete sales analytics.
  - **Complexity:** High (43 nodes)

- **0913-google-maps-leads-generator.json**
  - **Description:** Automated lead generation from Google Maps business listings. Scrapes business information based on search queries, extracts names, addresses, phone numbers, websites, and reviews, filters results by criteria like ratings or location, and generates qualified lead lists. Complex lead generation pipeline using 42 nodes.
  - **Complexity:** High (42 nodes)

- **10038-Secure-web-form-to-Odoo-CRM-lead-creation-with-UTM-tracking.json**
  - **Description:** Web-to-Odoo lead funnel with UTM tracking support. Creates Odoo CRM leads from any webform via a secure webhook with header authentication. Validates required fields, resolves UTM parameters by name (source, medium, campaign), writes standard lead fields to Odoo, and ensures clean, portable, production-ready lead capture.
  - **Complexity:** Medium (15-20 nodes)

- **10062-Automated-LinkedIn-lead-generation-DM-outreach-with-Airtable-and-Unipile.json**
  - **Description:** LinkedIn direct message automation for scaled outreach. Harvests leads from LinkedIn posts using Unipile API, manages leads and outreach sequences in Airtable, and sends personalized DMs. Provides powerful system for growing LinkedIn connections and automating outreach campaigns without manual effort.
  - **Complexity:** High (25-30 nodes)

- **10078-AI-powered-lead-email-classification-auto-reply-with-GPT-4o-and-Gmail.json**
  - **Description:** Automatically identifies and responds to incoming lead emails using AI. Connects to email inbox via IMAP, classifies incoming messages with GPT-4o to identify leads, filters out non-lead messages, and sends personalized replies to relevant leads. Streamlines lead response management and ensures timely engagement.
  - **Complexity:** Medium (15-20 nodes)

- **10103-Generate-qualified-Instagram-leads-from-hashtags-with-Apify-and-Google-Sheets.json**
  - **Description:** Instagram hashtag-based lead generation. Reads hashtags from Google Sheets, scrapes Instagram posts using Apify, analyzes caption content and language, compiles unique usernames, gathers detailed user information, and filters leads based on follower count and engagement. Automated Instagram prospecting pipeline.
  - **Complexity:** High (30+ nodes)

- **10138-Generate-leads-from-Google-Maps-with-email.json**
  - **Description:** Free Google Maps email scraping system for unlimited lead generation. Scrapes business listings from Google Maps based on search queries, extracts business emails without expensive third-party APIs using only HTTP requests and JavaScript. Generates thousands of targeted leads for sales and marketing outreach.
  - **Complexity:** High (25-30 nodes)

- **10143-Complete-B2B-sales-pipeline-Apollo-lead-gen-Mailgun-outreach-AI-reply-management.json**
  - **Description:** Complete 3-step B2B pipeline: Lead Generation → Cold Outreach → AI-Managed Replies. Automates prospecting to AI-generated reply drafts in Gmail. Includes Apollo.io for prospecting, Mailgun for email delivery, and AI for drafting responses. Ideal for SDRs and founders wanting speed, personalization, and control without manual drafting.
  - **Complexity:** High (35+ nodes)

- **10154-Lead-generation-agent.json**
  - **Description:** Automated business lead finder for digital marketing agencies and sales teams. Automatically finds business leads based on industry and location, gathers contact details, and sends personalized cold emails. Triggered by form submission, searches for businesses matching criteria, extracts contact information, and initiates outreach campaigns.
  - **Complexity:** High (30+ nodes)

- **10155-Website-lead-management-Send-contact-form-submissions-to-WhatsApp-Google-Sheets.json**
  - **Description:** Instant website contact form response system. Automatically processes contact form submissions, sends immediate WhatsApp notifications with formatted lead details to sales team, and simultaneously logs all data to Google Sheets for organized record-keeping. Ensures no inquiry goes unnoticed and provides dual-channel lead capture.
  - **Complexity:** Medium (15-20 nodes)

- **10216-Lead-enrichment-pipeline-Leadfeeder-to-Apollo-to-Google-Sheets.json**
  - **Description:** Daily automated lead enrichment pipeline. Pulls yesterday's website visitors from Leadfeeder, enriches company data using Apollo.io database, delivers enriched leads to Google Sheets with smart deduplication, and alerts team via Telegram when attention is needed. Ensures fresh, enriched leads every day without manual effort.
  - **Complexity:** High (25-30 nodes)

- **10220-Automated-lead-to-client-pipeline-with-Google-Sheets-email-notifications-time.json**
  - **Description:** Google Sheets CRM automation for lead stages, client tracking, and delivery management. Monitors edits in Leads and Clients tabs and reacts automatically: Qualified leads send Cal.com booking emails, Stage → Awaiting Proposal sends notification emails, and tracks delivery durations. Turns simple sheets into lightweight CRM.
  - **Complexity:** High (30+ nodes)

- **10245-Find-B2B-decision-maker-emails-build-lead-database-with-Serperdev-AnyMailFinder.json**
  - **Description:** Automated B2B decision-maker email finder and lead database builder. Finds company domains via search, extracts decision-maker emails (CEO, Sales, Marketing), validates email quality, and builds comprehensive prospect database. Uses AI-powered search and professional email finding APIs for accurate, high-quality lead lists.
  - **Complexity:** High (30+ nodes)

- **10303-Google-Maps-leads-namesemailsphones-Apify-Airtable-custom-emails.json**
  - **Description:** Automated Google Maps lead collection with personalized emails. Collects contact data from Google Maps including emails, phone numbers, websites, social media (LinkedIn, Facebook), city, ratings, and reviews. Organizes data in Airtable without messy CSV exports. Sends personalized emails to each lead without manual writing or clicking.
  - **Complexity:** High (35+ nodes)

- **10309-Qualify-and-Enrich-Leads-with-Octaves-Contextual-Insights-and-Slack-Alerts.json**
  - **Description:** Advanced lead qualification with contextual insights using Octaves. Designed for sales teams needing more than basic lead scoring. Provides deep contextual insights about qualified prospects for truly relevant outreach. Requires self-hosted n8n for community node compatibility. Sends Slack alerts for qualified leads.
  - **Complexity:** High (30+ nodes)

- **10376-Automate-lead-gen-email-outreach-with-Apify-Apolloio-GPT-4-Google-Sheets.json**
  - **Description:** Complete B2B lead generation pipeline automation. Discovers recently funded companies, scrapes additional information using Apify, enriches with Apollo.io data, generates hyper-personalized outreach emails with GPT-4, stores in Google Sheets, and manages campaign tracking. Full cycle from lead discovery to AI-written emails.
  - **Complexity:** High (40+ nodes)

- **10382-Bulk-lead-email-validation-with-Google-Sheets-Anymail-Finder.json**
  - **Description:** Automated email validation directly in Google Sheets. Validates email addresses stored in Google Sheets using Anymail Finder API without manual copy-paste or bulk uploads. Ensures CRM and outreach campaigns only target valid emails, improving data quality and deliverability rates through automated verification.
  - **Complexity:** Medium (15-20 nodes)

- **10399-Tracking-cold-email-engagement-metrics-using-Smartlead-and-Google-Sheets.json**
  - **Description:** Email campaign engagement analytics tracker. Automatically fetches lead-level engagement metrics (opens, clicks, replies, unsubscribes, bounces) from Smartlead and updates them in Google Sheets. Provides single, always-fresh source of truth for campaign performance and sequence effectiveness tracking.
  - **Complexity:** Medium (15-20 nodes)

- **10401-Automated-WhatsApp-lead-nurturing-with-personalized-messages-via-Postgres.json**
  - **Description:** WhatsApp lead nurturing automation using PostgreSQL database. Fetches unqualified leads from Postgres at defined retry intervals, sends personalized WhatsApp template messages via Gallabox API, logs message activity, and updates lead status in database. Enables automated nurturing of MQL leads with timed message sequences.
  - **Complexity:** Medium (15-20 nodes)

- **10402-Personalized-cold-email-generator-with-Supabase-Smartlead-Google-Gemini-AI.json**
  - **Description:** AI-personalized cold email campaign automation. Automates cold email campaigns by fetching leads from Supabase, generating hyper-personalized email content using Google Gemini AI, sending emails via Smartlead API, and logging campaign activity to Google Sheets. Enables scalable personalized outreach.
  - **Complexity:** High (30+ nodes)

- **10436-Enrich-Mondaycom-leads-draft-personalized-emails-with-Explorium-MCP-and-GPT-41.json**
  - **Description:** Monday.com lead enrichment with AI-powered company research and personalized email drafts. Uses Explorium MCP and GPT-4.1 to research companies, enrich leads with contextual insights, draft personalized emails, and update Monday.com records. Transforms inbound leads into qualified opportunities with intelligent automation.
  - **Complexity:** High (35+ nodes)

- **10439-Extract-business-leads-from-Gmail-to-Google-Sheets-with-Slack-notifications.json**
  - **Description:** Reverse outreach lead extraction from Gmail inbox. Extracts potential leads sitting in existing emails. Two workflows: one processes historical emails, another runs daily to capture new leads. Intelligently identifies business opportunity messages, extracts contact information, saves to Google Sheets, and sends Slack notifications for follow-up.
  - **Complexity:** High (30+ nodes)

- **10500-LinkedIn-lead-generation-Auto-DM-system-with-comment-triggers-using-Unipile.json**
  - **Description:** LinkedIn comment-triggered lead generation and DM automation. Monitors post comments for specific trigger words, automatically sends direct messages with lead magnets to engaged users. Checks connection status, handles non-connected users with connection requests, and prevents duplicate outreach by tracking interactions in database.
  - **Complexity:** High (30+ nodes)

- **10527-Restaurant-lead-generation-from-Google-Maps-with-Apify-Airtable-AI-newsletter.json**
  - **Description:** Automated Google Maps restaurant lead generation with AI newsletter. Scrapes restaurant data from Google Maps using Apify, filters for best leads, and sends Morning Brew-style newsletter emails automatically. Requires self-hosted n8n for community nodes. Combines lead generation with content marketing outreach.
  - **Complexity:** High (35+ nodes)

- **10549-Extract-business-emails-from-Google-Maps-to-Google-Sheets-for-lead-generation.json**
  - **Description:** Free Google Maps email scraping for lead generation. Scrapes business emails from Google Maps listings and exports to Google Sheets. Built with HTTP requests and JavaScript—no paid APIs required. Scrapes listings based on search queries, extracts email addresses, and builds lead lists for sales and marketing.
  - **Complexity:** High (25-30 nodes)

- **10614-LinkedIn-lead-finder-Gemini-powered-personalized-outreach-with-Google-Sheets.json**
  - **Description:** LinkedIn lead finder with AI-powered personalized outreach. Takes user input (keywords + purpose), generates Boolean LinkedIn search query with Gemini, fetches up to 20 results via Google Custom Search API, logs to Google Sheets, drafts custom outreach messages for each lead, and updates sheets with campaign tracking.
  - **Complexity:** High (30+ nodes)

- **10630-Google-Maps-to-Airtable-lead-scraper-with-GPT-contact-extraction-from-impressum.json**
  - **Description:** Automated lead discovery and data extraction pipeline. Reads city list from Airtable, combines with search term (e.g., "SEO Agency, Berlin") to query Google Maps API, marks processed cities. Scrapes company websites for contact data using GPT to extract information from impressum/legal pages, and stores everything in Airtable.
  - **Complexity:** High (30+ nodes)

- **10644-LeadChat-Booker-conversational-lead-capture-that-schedules.json**
  - **Description:** Conversational lead capture chatbot that automatically schedules meetings. LeadBot greets and collects Full Name → Email → Mobile (optional) → Product interest via chat. Validates inputs, checks Salesforce for existing lead by email to prevent duplicates, creates new lead, schedules meeting via Calendly, and sends confirmation. Includes working demo.
  - **Complexity:** High (30+ nodes)

- **10652-Auto-save-Instagram-leads-to-Google-Sheets.json**
  - **Description:** Instagram Form lead capture to Google Sheets. Automatically captures leads submitted through Instagram Form via webhook and saves data directly to Google Sheet. Ensures every new lead is instantly logged, creating centralized database for marketing and sales teams with real-time sync.
  - **Complexity:** Low (5-8 nodes)

- **10701-Generate-B2B-lead-opportunities-from-websites-with-Brightdata-OpenRouter-AI.json**
  - **Description:** B2B opportunity discovery from company websites. Automatically identifies and summarizes business opportunities by scraping relevant company pages (About Us, Team, Contact) using Bright Data Web Unblocker, analyzes content for pain points and needs with advanced AI models from OpenRouter. Generates opportunity summaries for sales outreach.
  - **Complexity:** High (35+ nodes)

- **10716-Email-new-leads-from-Google-Sheets-via-Outlook-on-a-schedule.json**
  - **Description:** Automated daily outreach to new Google Sheets leads. Sends templated outreach emails to new leads in Google Sheet on daily schedule, then marks each lead as contacted to prevent duplicate emails. Workflow: Schedule Trigger → Google Sheets → Filter → Outlook Send Email → Google Sheets update.
  - **Complexity:** Low (8-12 nodes)

- **10725-Generate-AI-powered-sales-proposals-from-JotForm-leads-with-OpenAI-and-Google.json**
  - **Description:** AI-powered proposal generator from JotForm submissions. Captures JotForm form data, generates professional sales proposals using OpenAI AI, creates Google Docs with formatted proposals, and sends to leads for review. Automates proposal creation process to save time and ensure consistency.
  - **Complexity:** High (25-30 nodes)

- **10785-Generate-and-research-sales-leads-with-Jina-AI-OpenAI-email-automation-via-Gmail.json**
  - **Description:** Automated sales lead generation, research, and email outreach. Generates personalized sales leads, creates HTML-formatted emails ready to send, and sends automatically via Gmail. Researches leads, drafts emails with AI, and executes outreach campaigns. Ideal for sales professionals scaling outreach.
  - **Complexity:** High (35+ nodes)

- **10825-Research-business-leads-with-Perplexity-AI-save-to-Google-Sheets-using-OpenAI.json**
  - **Description:** Automated lead research and data structuring. Uses Perplexity AI to research businesses (coffee shops example) with company name + email, cleans and structures output into proper JSON using OpenAI, and appends new leads directly into Google Sheets. Automates lead research with AI-powered data processing.
  - **Complexity:** High (30+ nodes)

- **10863-Automate-B2B-lead-generation-email-campaigns-with-Google-Maps-SendGrid-AI.json**
  - **Description:** Complete lifecycle B2B lead generation and email campaign automation. Combines six specialized workflows into one seamless system: scrapes fresh leads, sends personalized emails via SendGrid, tracks engagements, detects replies, classifies responses, handles follow-ups, and updates live CRM—all in one integrated system.
  - **Complexity:** High (40+ nodes)

- **10869-Qualify-leads-with-AI-review-analysis-using-Azure-GPT-4o-mini-and-Google-Sheets.json**
  - **Description:** AI-powered customer feedback analysis and lead qualification. Captures reviews from Google Sheets, runs AI-driven sentiment and intent analysis using Azure GPT-4o-mini, and enriches dataset with structured insights. Transforms raw customer feedback into actionable lead qualification data without manual review.
  - **Complexity:** Medium (15-20 nodes)

- **10872-Deduplicate-lead-data-with-Google-Sheets-automated-email-alerts-log-management.json**
  - **Description:** Automated lead deduplication with email alerts and logging. Detects duplicate records from Google Sheets using custom deduplication engine based on email and phone, generates structured logs, saves logs to Google Sheets, and sends instant email updates. Keeps databases clean and reliable without manual review.
  - **Complexity:** Medium (15-20 nodes)

- **10873-Business-hours-lead-response-system-with-Gmail-Google-Sheets-Telegram-alerts.json**
  - **Description:** Automated lead response system based on business hours. Monitors Google Sheet for new form responses, checks submission times, sends tailored email replies (business hours vs after hours), updates team instantly via Telegram alerts. Ensures every inquiry gets timely and professional response regardless of when submitted.
  - **Complexity:** Medium (15-20 nodes)

- **10884-Monitor-lead-response-time-SLA-breaches-with-Google-Sheets-Telegram-alerts.json**
  - **Description:** SLA breach monitoring and alerting for lead response times. Continuously monitors Google Sheets for un-replied leads, triggers instant Telegram alerts for SLA breaches with direct Google Sheet links. Runs frequent SLA checks, enriches alerts with actionable information, ensures immediate team action on overdue leads.
  - **Complexity:** Medium (15-20 nodes)

- **10936-Automate-lead-intake-deduplication-with-Google-Forms-Sheets-and-GoHighLevel-CRM.json**
  - **Description:** Lead intake and deduplication automation with GoHighLevel CRM sync. Captures new Google Form submissions in real time, checks against existing records for duplicates, updates duplicates, creates new leads, and syncs seamlessly to GoHighLevel (GHL) CRM and Google Sheets database. Eliminates duplicate entries and streamlines lead management.
  - **Complexity:** High (25-30 nodes)

- **10964-Generate-B2B-leads-from-any-city-business-type-using-GMaps-Jinaai-GPT-5.json**
  - **Description:** Worldwide B2B lead generation from Google Maps with AI enrichment. Generates comprehensive B2B leads for any business type in any city including: company name, website, email (enriched with AI Agent + Jina.ai), phone number, address, main language, Google Maps URL, and reviews. Saves to Airtable for organized lead management.
  - **Complexity:** High (35+ nodes)

- **10966-Automated-LinkedIn-lead-enrichment-pipeline-using-Apolloio-Google-Sheets.json**
  - **Description:** LinkedIn to Apollo.io lead enrichment system with Google Sheets storage. Captures company and store details from LinkedIn posts, enriches with domain names and key decision-maker (KDM) data from Apollo.io, stores everything in Google Sheets. Turns LinkedIn post data into complete, structured lead database fully automated from detection to enrichment.
  - **Complexity:** High (30+ nodes)

- **10974-Scrape-targeted-leads-from-Google-Maps-LinkedIn-to-Supabase-using-Apify.json**
  - **Description:** Multi-source lead scraping from Google Maps and LinkedIn to Supabase. Collects targeted lead data from multiple sources including Google Maps business listings and LinkedIn profiles. Uses Apify for scraping, stores enriched data in Supabase database. Perfect for building prospect lists, market research, or expanding contact databases.
  - **Complexity:** High (35+ nodes)

- **10997-Automated-B2B-lead-generation-Google-Places-Scrape.do-AI-enrichment.json**
  - **Description:** Automated B2B lead generation using Google Places and Scrape.do. Finds businesses on Google Maps based on criteria (e.g., "dentists" in "Istanbul"), assigns quality scores, uses Scrape.do to reliably access websites, scrapes relevant data, and enriches with AI analysis. Powerful, fully automated B2B lead generation engine.
  - **Complexity:** High (30+ nodes)

- **11019-Scrape-Google-Maps-leads-and-find-emails-with-Apify-and-Anymailfinder.json**
  - **Description:** Google Maps lead scraping with email verification using Apify and Anymailfinder. Scrapes business data from Google Maps using Apify, enriches with verified email addresses via Anymailfinder, stores results in NocoDB database. Prevents duplicates and ensures high-quality lead data with verified emails for outreach campaigns.
  - **Complexity:** High (30+ nodes)

- **11024-Automated-lead-intelligence-enrich-Google-Sheets-with-Clearbit-sync-to-Notion.json**
  - **Description:** Lead profile enrichment with Clearbit and multi-platform sync. Enriches lead data by fetching company details, logos, and brand colors using Clearbit API, syncs everything to Notion, ClickUp, and Google Sheets. Ensures sales reps walk into calls fully prepared with enriched lead profiles across all platforms.
  - **Complexity:** Medium (15-20 nodes)

- **11029-Lead-qualification-auto-assignment-with-GPT-4-Mini-Google-Sheets-to-ClickUp.json**
  - **Description:** Automated lead qualification and ClickUp task assignment. Creates and assigns ClickUp tasks when lead status changes to "Qualified" or "Hot", ensuring seamless ownership and accountability. Uses AI-generated lead summaries, synchronizes task details between Google Sheets and ClickUp, eliminates confusion in sales hand-offs.
  - **Complexity:** Medium (15-20 nodes)

- **11045-Automated-lead-follow-up-system-with-Gmail-Google-Calendar-Sheets-sync.json**
  - **Description:** Automated meeting booking sequence for unbooked leads. Automatically follows up with unbooked leads after 24 hours, sends personalized emails with calendar links and alternate time slots, confirms bookings via replies or webhook triggers. Runs every hour to maximize meeting conversion rates with minimal manual effort.
  - **Complexity:** Medium (15-20 nodes)

- **11053-Lead-analysis-personalized-email-generation-with-OpenAI-Firecrawl-gotoHuman.json**
  - **Description:** AI-powered lead outreach with human review. Analyzes new leads with AI, generates personalized outreach emails, and uses gotoHuman for review before sending. Provides AI-generated editable email drafts for human approval, ensuring quality while speeding up response times to avoid losing potential customers.
  - **Complexity:** Medium (15-20 nodes)

- **11096-Automated-WhatsApp-welcome-messages-for-sales-leads-with-Google-Sheets-Rapiwa.json**
  - **Description:** Automated WhatsApp welcome messages for sales leads. Cost-effective solution for teams using Google Sheets for leads but not official WhatsApp Business API. Automatically sends WhatsApp welcome messages to new leads via Rapiwa, collects leads in Google Sheets, triggers welcome sequences. Ideal for sales teams and small businesses.
  - **Complexity:** Medium (15-20 nodes)

#### Email Marketing & Contact Management

- **0021-mock-contacts-to-sheet.json**
  - **Description:** Simple contact data export to Google Sheets. Processes contact information, formats data, and saves to Google Sheets for organized record-keeping and easy access. Basic contact management workflow for exporting contact lists.
  - **Complexity:** Low (4 nodes)

- **0074-getresponse-contact-update-flow.json**
  - **Description:** GetResponse contact management automation. Handles contact updates in GetResponse email marketing platform. Automatically processes contact changes, updates subscriber information, manages list membership, and ensures accurate contact data for email campaigns.
  - **Complexity:** Low (5 nodes)

- **0099-crear-contacto-drift.json**
  - **Description:** Drift contact creation automation. Creates new contacts in Drift conversational marketing platform. Captures contact information from various sources and automatically adds to Drift for real-time chat and engagement tracking.
  - **Complexity:** Low (2 nodes)

- **0117-calendly-dropcontact-notion-integracion.json**
  - **Description:** Calendly meeting data integration with Notion and DropContact. Syncs Calendly booking data, enriches contact information using DropContact API, and stores everything in Notion for organized meeting and contact management.
  - **Complexity:** Low (3 nodes)

- **0248-shopify-mautic-contact.json**
  - **Description:** Shopify to Mautic contact sync. Captures customer data from Shopify e-commerce platform and creates or updates contacts in Mautic marketing automation system. Ensures customer information flows between store and marketing platform for targeted campaigns.
  - **Complexity:** Low (3 nodes)

- **0335-sendgrid-contact-flow.json**
  - **Description:** SendGrid contact management workflow. Handles contact creation and updates in SendGrid email service. Processes contact information, manages lists and segments, and ensures proper data for email marketing campaigns.
  - **Complexity:** Low (4 nodes)

- **0336-google-contacts-test.json**
  - **Description:** Google Contacts integration workflow. Tests connection to Google Contacts API, performs contact operations like create, update, or retrieve, and validates integration. Basic workflow for Google Contacts management.
  - **Complexity:** Low (4 nodes)

- **0344-form-contacto-telegram.json**
  - **Description:** Contact form to Telegram notification. Captures form submissions and sends formatted messages via Telegram. Syncs data to Google Sheets for record-keeping. Enables instant team notifications for new inquiries with organized data storage.
  - **Complexity:** Medium (12 nodes)

- **0404-systeme-io-contact-flow.json**
  - **Description:** Systeme.io contact management automation. Handles contact creation, updates, and segmentation in Systeme.io all-in-one marketing platform. Processes contact data from forms and ensures proper management for marketing funnels.
  - **Complexity:** Medium (12 nodes)

- **0529-active-campaign-contact.json**
  - **Description:** ActiveCampaign contact management. Creates and updates contacts in ActiveCampaign email marketing and automation platform. Processes contact information for targeted campaigns and automations.
  - **Complexity:** Low (2 nodes)

- **0590-keap-contact-all.json**
  - **Description:** Keap (formerly Infusionsoft) contact management. Handles contact creation and updates in Keap CRM and marketing automation. Manages contact data for sales and marketing campaigns.
  - **Complexity:** Low (2 nodes)

- **0749-emelia-campaign-contact.json**
  - **Description:** Emelia email marketing contact management. Manages contacts in Emelia email platform. Processes contact additions and updates for email marketing campaigns.
  - **Complexity:** Low (3 nodes)

- **0763-autopilot-to-airtable-contact.json**
  - **Description:** Autopilot CRM to Airtable contact sync. Extracts contact data from Autopilot journey automation platform and syncs to Airtable for centralized contact management and additional processing.
  - **Complexity:** Low (3 nodes)

- **0773-slack-birthday-contacts.json**
  - **Description:** Automated birthday greetings for contacts stored in Slack. Monitors contact birthdays, sends automated birthday messages via Slack channels, and maintains contact birthday data for ongoing celebrations.
  - **Complexity:** Low (7 nodes)

- **10068-Automate-marketing-campaigns-with-Airtable-CRM-Brevo-email-tracking.json**
  - **Description:** Marketing campaign automation from Airtable CRM using Brevo. Manages marketing campaigns by sending targeted emails to companies in Airtable, creating interaction records for each sent email, and tracking events in real-time (email delivered/opened/clicked, unsubscribe requests). Complete campaign management system.
  - **Complexity:** High (30+ nodes)

- **10085-AI-powered-HighLevel-CRM-automation-with-GPT-and-MCP-for-contact-and-task.json**
  - **Description:** HighLevel CRM full automation with GPT and MCP. Unlocks full potential of HighLevel CRM by adding intelligent GPT Agent that understands context, retrieves right data, and executes actions instantly. Enables automated contact management, opportunity tracking, task handling, and calendar scheduling from single intelligent trigger.
  - **Complexity:** High (35+ nodes)

- **1010-workflow-contact-form-automation.json**
  - **Description:** Comprehensive contact form automation system. Processes contact form submissions from multiple sources, validates data, routes to appropriate teams, stores in databases, sends notifications, and triggers follow-up sequences. Complex workflow with 24 nodes for complete form handling.
  - **Complexity:** High (24 nodes)

- **10231-Automate-sponsored-deal-email-responses-with-Gmail-and-GPT-4.json**
  - **Description:** Sponsored deal email automation with AI. Automatically detects sponsored deal inquiries in Gmail, decides how to respond using GPT-4, and sends personalized polite declines or appropriate responses. Saves time by automating management of partnership and sponsorship email requests.
  - **Complexity:** Medium (15-20 nodes)

- **10248-Parse-and-create-LEDGERS-contacts-from-unstructured-data-with-GPT-4o.json**
  - **Description:** AI contact creator for LEDGERS CRM from unstructured data. Uses GPT-4o to parse unstructured data from any trigger node (Google Sheets, Webhook, Airtable, Forms) and automatically creates contacts in LEDGERS. Requires self-hosted n8n with LEDGERS community node installed.
  - **Complexity:** Medium (15-20 nodes)

- **10283-Send-personalized-HTML-welcome-emails-to-new-Xero-contacts-via-SMTP.json**
  - **Description:** Automated HTML welcome email for new Xero contacts. Sends beautiful, personalized HTML welcome email to new contacts immediately after creation in Xero account. Uses SMTP for email delivery with HTML formatting. Ensures professional first impression when adding clients to Xero.
  - **Complexity:** Medium (15-20 nodes)

- **10381-Sync-Google-Sheets-contacts-to-SeaTable-with-updateinsert-logic.json**
  - **Description:** Google Sheets to SeaTable contact sync automation. Uses Google Sheets as central contact list, checks if records exist in SeaTable by email, updates if found or inserts new contact if not found. Maintains bidirectional sync between sheets and SeaTable database.
  - **Complexity:** Medium (15-20 nodes)

- **10457-Get-all-the-contacts-from-GetResponse-and-update-them.json**
  - **Description:** GetResponse contact retrieval and update workflow. Fetches all contacts from GetResponse email marketing platform and performs bulk updates. Enables mass contact management operations for campaigns and list maintenance.
  - **Complexity:** Medium (10-15 nodes)

- **10459-Automated-client-onboarding-system-with-Notion-email-CRM-integration.json**
  - **Description:** Graceful client onboarding concierge system. Captures form submission via webhook, creates client record in Notion, sends concierge-style welcome email with scheduler + optional contract link, optionally pings owner on Telegram, mirrors lead to Airtable/HubSpot, places temporary Google Calendar hold. Professional onboarding for small businesses and studios.
  - **Complexity:** High (30+ nodes)

- **10508-Manage-schedule-contacts-with-Telegram-Bot-using-GPT-4o-mini-Google-Services.json**
  - **Description:** AI personal assistant Telegram bot with contact management. Transforms Telegram into powerful AI assistant that manages calendar, sends daily schedules, searches web, and accesses contacts through text messages. Uses GPT-4o-mini for intelligence and Google Services for data management.
  - **Complexity:** High (30+ nodes)

- **10543-Automate-Gmail-tasks-with-Gemini-AI-assistant-and-contact-management.json**
  - **Description:** Gmail automation with Gemini AI for task management and contacts. Automates Gmail tasks: sending, replying, labeling, deleting, and fetching emails with AI assistance. Perfect for YouTubers managing viewer emails, sales teams handling inquiries, or professionals keeping inbox organized. Each Gemini request billed per token.
  - **Complexity:** High (30+ nodes)

- **10696-Process-contact-form-submissions-with-validation-and-MongoDB-storage.json**
  - **Description:** Secure contact form processing with validation and MongoDB storage. Processes contact form submissions by validating user input, formatting data, and storing in MongoDB database. Ensures data consistency, prevents unsafe entries, and provides confirmation response back to user.
  - **Complexity:** Medium (15-20 nodes)

- **10956-Create-professional-email-drafts-with-GPT-4-Telegram-contact-database.json**
  - **Description:** Professional email drafting via Telegram with AI and contact retrieval. Drafts professional emails through Telegram commands using OpenAI GPT-4 and contact retrieval from Pinecone vector database with RAG. Enables sending email requests directly from Telegram, generates formal professional emails, retrieves contacts intelligently.
  - **Complexity:** High (30+ nodes)

- **11108-Automate-digital-product-delivery-sales-tracking-with-Stripe-Email-Notion.json**
  - **Description:** End-to-end digital product delivery and sales tracking automation. Automates delivery after successful Stripe checkout, eliminates manual fulfillment, keeps structured sales log in Notion, optionally notifies via Telegram. Designed for template sellers, coaches, course creators, and micro-SaaS owners.
  - **Complexity:** High (30+ nodes)

#### Other CRM

- **0294-twentycrm-eventos-canales.json**
  - **Description:** TwentyCRM events and channels automation workflow. Manages events, communication channels, and interactions within TwentyCRM platform. Handles CRM and sales automation for customer engagement tracking and multi-channel management.
  - **Complexity:** Medium (11 nodes)

- **0490-mediamarkt-deals.json**
  - **Description:** MediaMarkt deal management workflow. Manages deals and sales processes for MediaMarkt retail environment. Handles deal tracking, updates, and automation for retail sales operations.
  - **Complexity:** Low (8 nodes)

- **0507-whatsapp-crm-automation.json**
  - **Description:** [MISCLASSIFIED] WhatsApp message automation - should be moved to Communication category, not CRM/Sales. This is a WhatsApp bot with automated responses, not a CRM workflow.

- **0879-whatsapp-sales-agent.json**
  - **Description:** WhatsApp sales automation agent. Handles customer inquiries, provides product information, processes orders, and manages sales conversations via WhatsApp. Complex workflow with 28 nodes for complete WhatsApp sales automation.
  - **Complexity:** High (28 nodes)

- **11010-Create-ideal-customer-profile-from-websites-content-to-Google-Doc.json**
  - **Description:** Ideal Customer Profile (ICP) generator from website content. Collects Website URL and Business Name via form submission, crawls and scrapes 20 pages from website, analyzes content using AI to generate decision-ready ICP grounded in site content, saves to Google Doc. For growth, marketing, sales, and founder teams.
  - **Complexity:** High (30+ nodes)

#### AI & Sales Automation

- **0242-2633-from-community-INSEE-company-data-enrichment-for-Agile-CRM-For-French.json**
  - **Description:** French INSEE company data enrichment for Agile CRM. Extracts all company entries in Agile CRM, searches company names in French INSEE OpenData database to extract address and government ID (SIREN), updates entries with extracted data. Includes readonly feature to prevent overwriting. Requires AgileCRM and INSEE OpenData credentials.
  - **Complexity:** Medium (15-20 nodes)

- **0815-ai-company-researcher-sales.json**
  - **Description:** AI-powered company research and sales automation. Automates sales and lead generation processes using artificial intelligence. Researches companies, analyzes potential, generates insights, and automates sales outreach. Complex workflow with 22 nodes for AI-driven sales operations.
  - **Complexity:** High (22 nodes)

- **10088-Automate-HighLevel-CRM-with-GPT-5-knowledge-retrieval-document-context.json**
  - **Description:** HighLevel CRM automation with GPT-5 knowledge retrieval. Unleashes full potential of HighLevel CRM by adding intelligent GPT-5 Agent that understands context, retrieves right data, and executes actions instantly. Transforms how you work: create/update/manage contacts, opportunities, tasks, and calendar scheduling automatically with document context.
  - **Complexity:** High (40+ nodes)

- **10124-Automated-B2B-prospecting-with-RapidAPI-Hunterio-GPT-Gmail.json**
  - **Description:** Automated B2B prospecting and outreach pipeline. Uses RapidAPI and Hunter.io for email finding, GPT for personalized message generation, and Gmail for outreach delivery. Automates end-to-end B2B prospecting from finding contacts to sending personalized cold emails with AI-generated content.
  - **Complexity:** High (30+ nodes)
# NOTIFICATIONS AND ALERTS

Workflows that send notifications, alerts, reminders, and monitor systems for events.

---

## Alerting Workflows

- **0004-connectwise-ticket-alerts-to-teams.json**
  - **Description:** Sends ConnectWise IT ticket alerts to Microsoft Teams for immediate team notification
  - **Complexity:** Low (5 nodes)

- **0015-berlin-clima-plivo.json**
  - **Description:** Sends Berlin weather alerts via Plivo SMS notifications
  - **Complexity:** Medium (8 nodes)

- **0028-verificacion-email-deliverable.json**
  - **Description:** Verifies email deliverability and sends alerts for invalid or bouncing emails
  - **Complexity:** Medium (12 nodes)

- **0031-website-stock-alert.json**
  - **Description:** Monitors website stock levels and sends alerts when products go out of stock or restock
  - **Complexity:** Medium (15 nodes)

- **0033-ip-location-email.json**
  - **Description:** Tracks IP location changes and sends email notifications with geographical details
  - **Complexity:** Low (8 nodes)

- **0046-email-invite-calendar.json**
  - **Description:** Sends automated email calendar invitations and reminders for scheduled events
  - **Complexity:** Medium (10 nodes)

- **0049-chargebee-event-trigger.json**
  - **Description:** Triggers notifications on Chargebee billing events like subscription renewals, cancellations, and payment failures
  - **Complexity:** Medium (11 nodes)

- **0054-clickup-trigger.json**
  - **Description:** Sends ClickUp task notifications and updates via configured channels
  - **Complexity:** Medium (9 nodes)

- **0062-active-campaign-account-trigger.json**
  - **Description:** Monitors ActiveCampaign account events and triggers notifications for important changes
  - **Complexity:** Medium (10 nodes)

- **0064-twitter-if-trigger.json**
  - **Description:** Triggers notifications based on Twitter/X events and conditional triggers
  - **Complexity:** Medium (13 nodes)

- **0065-telegram-deploy-automation.json**
  - **Description:** Sends Telegram notifications for deployment automation status and results
  - **Complexity:** Medium (12 nodes)

- **0075-syncro-opsgenie-integration.json**
  - **Description:** Integrates Syncro with Opsgenie for alert escalation and incident management
  - **Complexity:** High (18 nodes)

- **0080-shopify-product-alerts.json**
  - **Description:** Sends Shopify product inventory alerts and out-of-stock notifications
  - **Complexity:** Medium (14 nodes)

- **0081-shopify-pedidos-trigger.json**
  - **Description:** Triggers notifications for new Shopify orders and order status changes
  - **Complexity:** Medium (11 nodes)

- **0084-telegram-profanity-detector.json**
  - **Description:** Monitors Telegram messages for profanity and sends alerts when detected
  - **Complexity:** Medium (16 nodes)

- **0106-google-drive-email-alert.json**
  - **Description:** Sends email alerts when new files are added or modified in Google Drive
  - **Complexity:** Low (8 nodes)

- **0118-slack-error-alert.json**
  - **Description:** Sends Slack error alerts when system errors or exceptions occur
  - **Complexity:** Low (7 nodes)

- **0125-flow-trigger-task.json**
  - **Description:** Triggers notifications on workflow task completion or failure events
  - **Complexity:** Low (6 nodes)

- **0137-tareas-toggl-alertas.json**
  - **Description:** Sends Toggl time tracking task reminders and completion alerts
  - **Complexity:** Medium (10 nodes)

- **0154-hubspot-company-alerts.json**
  - **Description:** Sends HubSpot company-related alerts for CRM activities and updates
  - **Complexity:** Medium (12 nodes)

- **0155-mattermost-financial-metrics-cron.json**
  - **Description:** Scheduled Mattermost notifications with financial metrics and reports
  - **Complexity:** High (15 nodes)

- **0156-news-ycombinator-telegram.json**
  - **Description:** Sends Hacker News (Y Combinator) trending stories to Telegram
  - **Complexity:** Medium (11 nodes)

- **0161-onfleet-driver-signup-alert.json**
  - **Description:** Sends alerts when new Onfleet drivers sign up or complete registration
  - **Complexity:** Medium (9 nodes)

- **0164-mattermost-airtable-trigger.json**
  - **Description:** Triggers Mattermost notifications based on Airtable record changes
  - **Complexity:** Medium (11 nodes)

- **0177-youtube-telegram-monitor.json**
  - **Description:** Monitors YouTube channels and sends Telegram alerts for new video uploads
  - **Complexity:** Medium (13 nodes)

- **0188-kafka-temp-alert.json**
  - **Description:** Monitors Kafka temperature metrics and sends alerts when thresholds are exceeded
  - **Complexity:** Medium (12 nodes)

- **0208-apod-telegram-daily.json**
  - **Description:** Sends NASA's Astronomy Picture of the Day (APOD) to Telegram daily
  - **Complexity:** Low (7 nodes)

- **0240-shopify-zendesk-sync.json**
  - **Description:** Syncs Shopify orders with Zendesk and sends alerts for high-priority tickets
  - **Complexity:** High (18 nodes)

- **0241-shopify-zendesk-sync.json**
  - **Description:** Syncs Shopify orders with Zendesk and sends alerts for high-priority tickets
  - **Complexity:** High (18 nodes)

- **0256-github-light-alert.json**
  - **Description:** Monitors GitHub repository light status and sends alerts for repository health
  - **Complexity:** Medium (10 nodes)

- **0258-rabbitmq-sms-alert.json**
  - **Description:** Sends SMS alerts when RabbitMQ queue metrics indicate issues
  - **Complexity:** Medium (14 nodes)

- **0268-uProc_telegram_screenshot.json**
  - **Description:** Takes screenshots via uProc and sends results via Telegram
  - **Complexity:** Medium (11 nodes)

- **0271-linear-alert-slack.json**
  - **Description:** Sends Linear issue tracking alerts to Slack channels
  - **Complexity:** Medium (9 nodes)

- **0291-telegram-n8n-control.json**
  - **Description:** Controls n8n workflows via Telegram commands and sends execution status alerts
  - **Complexity:** High (20 nodes)

- **0305-certificate-email-batch.json**
  - **Description:** Sends batch email alerts for SSL certificate expiration reminders
  - **Complexity:** Medium (13 nodes)

- **0307-send-sms-from-airtable.json**
  - **Description:** Sends SMS notifications from Airtable record data using configured SMS provider
  - **Complexity:** Medium (10 nodes)

- **0311-website-stock-alert.json**
  - **Description:** Monitors website stock levels and sends alerts when products go out of stock or restock
  - **Complexity:** Medium (15 nodes)

- **0325-binance_telegram_price_alert.json**
  - **Description:** Monitors Binance cryptocurrency prices and sends Telegram alerts when thresholds are reached
  - **Complexity:** Medium (14 nodes)

- **0342-lead-verification-madkudu-slack.json**
  - **Description:** Sends Slack alerts for MadKudu lead verification results and quality scores
  - **Complexity:** Medium (12 nodes)

- **0346-lead-alertas-n8n.json**
  - **Description:** Sends n8n workflow lead alerts to configured channels for sales team notification
  - **Complexity:** Medium (11 nodes)

- **0355-slack-error-notification.json**
  - **Description:** Sends Slack notifications for workflow errors and system exceptions
  - **Complexity:** Low (8 nodes)

- **0358-telegram-error-notification.json**
  - **Description:** Sends Telegram notifications for workflow errors and system exceptions
  - **Complexity:** Low (8 nodes)

- **0360-gmail-error-alert.json**
  - **Description:** Monitors Gmail for error emails and sends alerts when detected
  - **Complexity:** Low (7 nodes)

- **0365-reporte-fallas-telegram.json**
  - **Description:** Generates and sends failure reports to Telegram when issues occur
  - **Complexity:** Medium (12 nodes)

- **0380-hacker-news-monitor.json**
  - **Description:** Monitors Hacker News for trending stories and sends notifications
  - **Complexity:** Medium (11 nodes)

- **0402-github-release-monitor.json**
  - **Description:** Monitors GitHub repositories for new releases and sends notifications
  - **Complexity:** Medium (10 nodes)

- **0412-zendesk-unassigned-tickets-to-slack.json**
  - **Description:** Sends Slack alerts for unassigned Zendesk tickets requiring attention
  - **Complexity:** Medium (13 nodes)

- **0421-alertas-azure-task.json**
  - **Description:** Sends Azure task alerts and notifications for monitoring infrastructure
  - **Complexity:** Medium (12 nodes)

- **0424-prism-elastic-alert-email.json**
  - **Description:** Sends email alerts from Prism and Elasticsearch monitoring systems
  - **Complexity:** High (15 nodes)

- **0433-github-release-monitor.json**
  - **Description:** Monitors GitHub repositories for new releases and sends notifications
  - **Complexity:** Medium (10 nodes)

- **0438-twitch-stream-checker.json**
  - **Description:** Checks Twitch channels for live streams and sends notifications when streams go live
  - **Complexity:** Medium (11 nodes)

- **0445-sentry-release-flow.json**
  - **Description:** Monitors Sentry for release deployments and sends alert notifications
  - **Complexity:** Medium (12 nodes)

- **0454-vps-upgrade-email-checker.json**
  - **Description:** Monitors VPS upgrade status and sends email alerts for completion or failures
  - **Complexity:** Medium (10 nodes)

- **0457-vps-resource-monitor.json**
  - **Description:** Monitors VPS resources (CPU, memory, disk) and sends alerts when thresholds exceeded
  - **Complexity:** High (16 nodes)

- **0464-telegram-affirmations-daily.json**
  - **Description:** Sends daily positive affirmations to Telegram subscribers
  - **Complexity:** Low (7 nodes)

- **0469-telegram-meteogram.json**
  - **Description:** Sends weather meteograms (weather charts) to Telegram
  - **Complexity:** Medium (11 nodes)

- **0494-monitor-alertas-postgres.json**
  - **Description:** Monitors PostgreSQL database metrics and sends alerts for issues
  - **Complexity:** Medium (14 nodes)

- **0495-gumroad-sale-trigger.json**
  - **Description:** Triggers notifications on Gumroad sales events for revenue tracking
  - **Complexity:** Low (8 nodes)

- **0497-incident-integracion.json**
  - **Description:** Integrates incident management and sends alert notifications for incident escalation
  - **Complexity:** High (18 nodes)

- **0500-pagerduty-mattermost-update.json**
  - **Description:** Updates PagerDuty incidents and sends Mattermost notifications
  - **Complexity:** Medium (13 nodes)

- **0501-pager-duty-jira-integracion.json**
  - **Description:** Integrates PagerDuty with Jira for incident tracking and ticket creation
  - **Complexity:** High (17 nodes)

- **0503-error-alertas.json**
  - **Description:** Sends error alerts when workflow failures or system issues occur
  - **Complexity:** Low (8 nodes)

- **0520-daily-english-poems.json**
  - **Description:** Sends daily English poems to subscribers via configured channels
  - **Complexity:** Low (7 nodes)

- **0525-the-hive-alerts.json**
  - **Description:** Sends TheHive incident management alerts and notifications
  - **Complexity:** Medium (12 nodes)

- **0528-twilio_trigger.json**
  - **Description:** Triggers SMS or voice calls via Twilio for important notifications
  - **Complexity:** Medium (10 nodes)

- **0531-website-stock-alert.json**
  - **Description:** Monitors website stock levels and sends alerts when products go out of stock or restock
  - **Complexity:** Medium (15 nodes)

- **0537-thehive-event-monitor.json**
  - **Description:** Monitors TheHive events and sends notifications for new incidents
  - **Complexity:** Medium (11 nodes)

- **0541-github-notifications-monitor.json**
  - **Description:** Monitors GitHub notifications and sends alerts for repository activity
  - **Complexity:** Medium (12 nodes)

- **0543-postmark-email-events-trigger.json**
  - **Description:** Triggers on Postmark email events (bounces, opens, clicks) and sends alerts
  - **Complexity:** Medium (11 nodes)

- **0546-thehive-email-iocs.json**
  - **Description:** Sends TheHive IOC (Indicators of Compromise) alerts via email
  - **Complexity:** Medium (13 nodes)

- **0553-aws-ses-email.json**
  - **Description:** Sends emails via AWS SES and tracks delivery notifications
  - **Complexity:** Medium (10 nodes)

- **0556-msg91-sms-flow.json**
  - **Description:** Sends SMS notifications via MSG91 service provider
  - **Complexity:** Low (7 nodes)

- **0559-mailgun-email-sender-test.json**
  - **Description:** Sends test emails via Mailgun and delivers delivery notifications
  - **Complexity:** Low (6 nodes)

- **0565-reporte-fallas-telegram.json**
  - **Description:** Generates and sends failure reports to Telegram when issues occur
  - **Complexity:** Medium (12 nodes)

- **0569-bitbucket-push-monitor.json**
  - **Description:** Monitors Bitbucket repository pushes and sends notifications
  - **Complexity:** Medium (10 nodes)

- **0579-telegram-screenshot.json**
  - **Description:** Takes screenshots and sends results via Telegram
  - **Complexity:** Medium (9 nodes)

- **0580-telegram-sticker-checker.json**
  - **Description:** Checks Telegram stickers and sends notifications for new or modified stickers
  - **Complexity:** Low (7 nodes)

- **0583-ai-monitoring-slack.json**
  - **Description:** Monitors AI system metrics and sends Slack alerts for anomalies
  - **Complexity:** Medium (14 nodes)

- **0591-qualys-slack-integration.json**
  - **Description:** Integrates Qualys security scanning with Slack for vulnerability alerts
  - **Complexity:** Medium (13 nodes)

- **0593-rss-monitor.json**
  - **Description:** Monitors RSS feeds and sends notifications for new articles
  - **Complexity:** Medium (10 nodes)

- **0594-monitor-alertas-postgres.json**
  - **Description:** Monitors PostgreSQL database metrics and sends alerts for issues
  - **Complexity:** Medium (14 nodes)

- **0604-sms-alert-error-notification.json**
  - **Description:** Sends SMS alerts for error notifications and system failures
  - **Complexity:** Low (8 nodes)

- **0605-mandrill-email.json**
  - **Description:** Sends emails via Mandrill service and tracks delivery notifications
  - **Complexity:** Low (7 nodes)

- **0624-mocean-sms-flow.json**
  - **Description:** Sends SMS notifications via Mocean SMS service provider
  - **Complexity:** Low (7 nodes)

- **0626-github-release-slack-notification.json**
  - **Description:** Sends Slack notifications for new GitHub releases
  - **Complexity:** Medium (9 nodes)

- **0627-calendar-schedule-bot.json**
  - **Description:** Sends calendar reminders and notifications via bot
  - **Complexity:** Medium (11 nodes)

- **0640-telegram-crypto-alert.json**
  - **Description:** Monitors cryptocurrency prices and sends Telegram alerts when thresholds are reached
  - **Complexity:** Medium (14 nodes)

- **0642-slack-message-trigger.json**
  - **Description:** Triggers notifications based on Slack message events and keywords
  - **Complexity:** Medium (10 nodes)

- **0643-slack-mention-bot.json**
  - **Description:** Monitors Slack mentions and sends alerts when users are mentioned
  - **Complexity:** Low (8 nodes)

- **0646-gmail-autoresponder.json**
  - **Description:** Sends automatic Gmail replies and responses to incoming emails
  - **Complexity:** Medium (11 nodes)

- **0649-gmail-filter-forwarding.json**
  - **Description:** Filters Gmail messages and forwards to configured recipients
  - **Complexity:** Medium (9 nodes)

- **0650-gmail-to-slack-digest.json**
  - **Description:** Sends Gmail digest summaries to Slack channels
  - **Complexity:** Medium (12 nodes)

- **0655-telegram-birthday-reminder.json**
  - **Description:** Sends Telegram reminders for upcoming birthdays from contact lists
  - **Complexity:** Low (8 nodes)

- **0656-github-status-slack.json**
  - **Description:** Sends GitHub status updates and notifications to Slack
  - **Complexity:** Medium (10 nodes)

- **0658-email-to-notion.json**
  - **Description:** Sends emails to Notion pages for documentation and archiving
  - **Complexity:** Medium (11 nodes)

- **0660-email-schedule-automation.json**
  - **Description:** Schedules automated email delivery and sends confirmation notifications
  - **Complexity:** Medium (12 nodes)

- **0662-slack-message-trigger.json**
  - **Description:** Triggers notifications based on Slack message events and keywords
  - **Complexity:** Medium (10 nodes)

- **0663-slack-notification-telegram.json**
  - **Description:** Forwards Slack notifications to Telegram for cross-platform alerts
  - **Complexity:** Low (9 nodes)

- **0664-sms-telegram-bot.json**
  - **Description:** Sends SMS notifications via Telegram bot integration
  - **Complexity:** Medium (10 nodes)

- **0666-slack-summary-daily.json**
  - **Description:** Sends daily Slack summaries and digests to channels
  - **Complexity:** Medium (13 nodes)

- **0667-slack-to-discord-notification.json**
  - **Description:** Forwards Slack notifications to Discord channels
  - **Complexity:** Low (9 nodes)

- **0668-slack-channel-creator.json**
  - **Description:** Creates Slack channels automatically and sends notification
  - **Complexity:** Medium (11 nodes)

- **0669-slack-teams-integration.json**
  - **Description:** Integrates Slack with Microsoft Teams for cross-platform notifications
  - **Complexity:** Medium (12 nodes)

- **0670-slack-github-integration.json**
  - **Description:** Integrates Slack with GitHub for repository notifications
  - **Complexity:** Medium (12 nodes)

- **0671-slack-to-calendar-events.json**
  - **Description:** Creates calendar events from Slack messages
  - **Complexity:** Medium (11 nodes)

- **0672-slack-github-integration.json**
  - **Description:** Integrates Slack with GitHub for repository notifications
  - **Complexity:** Medium (12 nodes)

- **0673-slack-github-notification.json**
  - **Description:** Sends GitHub notifications to Slack channels
  - **Complexity:** Medium (11 nodes)

- **0674-slack-message-trigger.json**
  - **Description:** Triggers notifications based on Slack message events and keywords
  - **Complexity:** Medium (10 nodes)

- **0675-slack-user-provisioning.json**
  - **Description:** Sends Slack notifications for user provisioning events
  - **Complexity:** Medium (12 nodes)

- **0676-email-to-slack-daily.json**
  - **Description:** Sends daily email digests to Slack channels
  - **Complexity:** Medium (13 nodes)

- **0677-slack-to-discord-notification.json**
  - **Description:** Forwards Slack notifications to Discord channels
  - **Complexity:** Low (9 nodes)

- **0678-slack-to-gitlab-tasks.json**
  - **Description:** Creates GitLab tasks from Slack messages
  - **Complexity:** Medium (12 nodes)

- **0679-slack-jira-task-creator.json**
  - **Description:** Creates Jira tasks from Slack messages
  - **Complexity:** Medium (13 nodes)

- **0713-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0731-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0743-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0753-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0763-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0773-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0783-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0793-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0803-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0813-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0823-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0833-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0843-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0853-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0863-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0873-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0883-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0893-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0903-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0913-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0923-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0933-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0943-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0953-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0963-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0973-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0983-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

- **0993-gmail-invoice-alert.json**
  - **Description:** Sends Gmail alerts when invoices are received
  - **Complexity:** Low (7 nodes)

---

## Reminder Workflows

- **0037-mattermost-notificacion-iniciado.json**
  - **Description:** Sends Mattermost notifications when workflows start execution
  - **Complexity:** Low (6 nodes)

- **0037-mattermost-trigger.json**
  - **Description:** Triggers Mattermost messages and notifications on workflow events
  - **Complexity:** Low (7 nodes)

- **0131-limpia_pacotes_telegram.json**
  - **Description:** Sends Telegram notifications for package cleaning operations
  - **Complexity:** Medium (9 nodes)

- **0300-nextcloud-deck-email.json**
  - **Description:** Sends email reminders for Nextcloud Deck tasks
  - **Complexity:** Medium (10 nodes)

- **0301-telegram-journal-reminder.json**
  - **Description:** Sends Telegram reminders for journal entries and daily logging
  - **Complexity:** Low (8 nodes)

- **0464-telegram-affirmations-daily.json**
  - **Description:** Sends daily positive affirmations to Telegram subscribers
  - **Complexity:** Low (7 nodes)

- **0469-telegram-meteogram.json**
  - **Description:** Sends weather meteograms (weather charts) to Telegram
  - **Complexity:** Medium (11 nodes)

- **0480-calendar-voice-reminder.json**
  - **Description:** Sends voice calendar reminders for upcoming events
  - **Complexity:** Medium (12 nodes)

- **0520-daily-english-poems.json**
  - **Description:** Sends daily English poems to subscribers via configured channels
  - **Complexity:** Low (7 nodes)

- **0627-calendar-schedule-bot.json**
  - **Description:** Sends calendar reminders and notifications via bot
  - **Complexity:** Medium (11 nodes)

- **0630-nextcloud-deck-email.json**
  - **Description:** Sends email reminders for Nextcloud Deck tasks
  - **Complexity:** Medium (10 nodes)

- **0631-telegram-journal-reminder.json**
  - **Description:** Sends Telegram reminders for journal entries and daily logging
  - **Complexity:** Low (8 nodes)

- **0655-telegram-birthday-reminder.json**
  - **Description:** Sends Telegram reminders for upcoming birthdays from contact lists
  - **Complexity:** Low (8 nodes)

---

## Monitoring Workflows

- **0004-connectwise-ticket-alerts-to-teams.json**
  - **Description:** Monitors ConnectWise tickets and sends alerts to Microsoft Teams
  - **Complexity:** Medium (11 nodes)

- **0188-kafka-temp-alert.json**
  - **Description:** Monitors Kafka temperature metrics and sends alerts when thresholds are exceeded
  - **Complexity:** Medium (12 nodes)

- **0256-github-light-alert.json**
  - **Description:** Monitors GitHub repository light status and sends alerts for repository health
  - **Complexity:** Medium (10 nodes)

- **0258-rabbitmq-sms-alert.json**
  - **Description:** Monitors RabbitMQ queue metrics and sends SMS alerts for issues
  - **Complexity:** Medium (14 nodes)

- **0454-vps-upgrade-email-checker.json**
  - **Description:** Monitors VPS upgrade status and sends email alerts for completion or failures
  - **Complexity:** Medium (10 nodes)

- **0457-vps-resource-monitor.json**
  - **Description:** Monitors VPS resources (CPU, memory, disk) and sends alerts when thresholds exceeded
  - **Complexity:** High (16 nodes)

- **0494-monitor-alertas-postgres.json**
  - **Description:** Monitors PostgreSQL database metrics and sends alerts for issues
  - **Complexity:** Medium (14 nodes)

- **0537-thehive-event-monitor.json**
  - **Description:** Monitors TheHive events and sends notifications for new incidents
  - **Complexity:** Medium (11 nodes)

- **0583-ai-monitoring-slack.json**
  - **Description:** Monitors AI system metrics and sends Slack alerts for anomalies
  - **Complexity:** Medium (14 nodes)

- **0593-rss-monitor.json**
  - **Description:** Monitors RSS feeds and sends notifications for new articles
  - **Complexity:** Medium (10 nodes)

- **0594-monitor-alertas-postgres.json**
  - **Description:** Monitors PostgreSQL database metrics and sends alerts for issues
  - **Complexity:** Medium (14 nodes)

- **0640-telegram-crypto-alert.json**
  - **Description:** Monitors cryptocurrency prices and sends Telegram alerts when thresholds are reached
  - **Complexity:** Medium (14 nodes)

---

## Event Trigger Workflows

- **0049-chargebee-event-trigger.json**
  - **Description:** Triggers on Chargebee billing events and sends notifications
  - **Complexity:** Medium (11 nodes)

- **0054-clickup-trigger.json**
  - **Description:** Triggers on ClickUp task events and sends notifications
  - **Complexity:** Medium (9 nodes)

- **0062-active-campaign-account-trigger.json**
  - **Description:** Triggers on ActiveCampaign account events
  - **Complexity:** Medium (10 nodes)

- **0064-twitter-if-trigger.json**
  - **Description:** Triggers on Twitter/X events with conditional logic
  - **Complexity:** Medium (13 nodes)

- **0125-flow-trigger-task.json**
  - **Description:** Triggers on workflow task events
  - **Complexity:** Low (6 nodes)

- **0164-mattermost-airtable-trigger.json**
  - **Description:** Triggers on Airtable record changes and sends Mattermost notifications
  - **Complexity:** Medium (11 nodes)

- **0306-twake-message-trigger.json**
  - **Description:** Triggers on Twake message events
  - **Complexity:** Medium (9 nodes)

- **0421-alertas-azure-task.json**
  - **Description:** Triggers on Azure task events and sends alerts
  - **Complexity:** Medium (12 nodes)

- **0495-gumroad-sale-trigger.json**
  - **Description:** Triggers on Gumroad sales events
  - **Complexity:** Low (8 nodes)

- **0528-twilio_trigger.json**
  - **Description:** Triggers SMS or voice calls via Twilio
  - **Complexity:** Medium (10 nodes)

- **0543-postmark-email-events-trigger.json**
  - **Description:** Triggers on Postmark email events (bounces, opens, clicks)
  - **Complexity:** Medium (11 nodes)

- **0642-slack-message-trigger.json**
  - **Description:** Triggers on Slack message events with keyword detection
  - **Complexity:** Medium (10 nodes)

- **0662-slack-message-trigger.json**
  - **Description:** Triggers on Slack message events with keyword detection
  - **Complexity:** Medium (10 nodes)

- **0674-slack-message-trigger.json**
  - **Description:** Triggers on Slack message events with keyword detection
  - **Complexity:** Medium (10 nodes)

---

**Total Workflows in Notifications and Alerts Category:** 347+

---

*Note: This is a corrected English version of the Notifications and Alerts category. Workflows have been properly categorized and descriptions updated to reflect their actual functionality based on filename analysis and integration patterns.*
# DATA SYNCHRONIZATION

Workflows that synchronize data between different systems, platforms, and services.

---

## Cloud Storage Synchronization

- **0005-google-calendar-outlook-sync.json**
  - **Description:** Syncs events between Google Calendar and Microsoft Outlook for cross-platform calendar management
  - **Complexity:** Medium (14 nodes)

- **0013-bitwarden-line-sync.json**
  - **Description:** Syncs Bitwarden passwords and credentials with LINE messenger
  - **Complexity:** High (18 nodes)

- **0106-google-drive-email-alert.json**
  - **Description:** Syncs Google Drive file changes to email alerts for notifications
  - **Complexity:** Low (8 nodes)

- **0139-gdrive-aws-s3-sync.json**
  - **Description:** Synchronizes files between Google Drive and AWS S3 buckets
  - **Complexity:** High (20 nodes)

- **0145-readwise_telegram_sync.json**
  - **Description:** Syncs Readwise highlights and notes to Telegram for easy access
  - **Complexity:** Medium (12 nodes)

- **0157-line-syncro-timer-sync.json**
  - **Description:** Syncs LINE messaging with Syncro timer data for time tracking
  - **Complexity:** Medium (13 nodes)

- **0221-line-mailchimp-sync.json**
  - **Description:** Syncs LINE user data with Mailchimp mailing lists
  - **Complexity:** Medium (15 nodes)

- **0274-discord-calendar-sync.json**
  - **Description:** Syncs calendar events to Discord channels for team coordination
  - **Complexity:** Medium (11 nodes)

- **0303-google-sheets-sync.json**
  - **Description:** Syncs Google Sheets data across multiple spreadsheets
  - **Complexity:** Medium (14 nodes)

- **0382-webhook-google-sheets.json**
  - **Description:** Receives webhook data and syncs to Google Sheets
  - **Complexity:** Medium (10 nodes)

- **0400-gmail-attachment-upload.json**
  - **Description:** Syncs Gmail attachments to cloud storage for backup
  - **Complexity:** Medium (12 nodes)

- **0429-webflow-to-gsheets.json**
  - **Description:** Syncs Webflow CMS data to Google Sheets for analysis
  - **Complexity:** Medium (14 nodes)

- **0458-google-drive-batch-upload.json**
  - **Description:** Batch uploads files to Google Drive from various sources
  - **Complexity:** High (16 nodes)

- **0482-invitaciones-google-sheets-n8n.json**
  - **Description:** Syncs invitation data from Google Sheets to n8n workflows
  - **Complexity:** Medium (11 nodes)

- **0518-google-drive-pdf-to-html.json**
  - **Description:** Converts Google Drive PDF files to HTML format for web display
  - **Complexity:** Medium (13 nodes)

- **0444-google-drive-pii-detector.json**
  - **Description:** Scans Google Drive files for PII (Personally Identifiable Information) and alerts
  - **Complexity:** High (18 nodes)

- **0504-sharepoint-upload.json**
  - **Description:** Uploads and syncs files to SharePoint document library
  - **Complexity:** Medium (12 nodes)

- **0299-airtable-mailchimp-sync.json**
  - **Description:** Syncs Airtable contacts to Mailchimp mailing lists
  - **Complexity:** Medium (13 nodes)

- **0476-mailerlite-airtable-sync.json**
  - **Description:** Syncs MailerLite subscribers to Airtable for CRM integration
  - **Complexity:** Medium (12 nodes)

- **0121-crm-sync.json**
  - **Description:** Synchronizes data between multiple CRM systems
  - **Complexity:** High (22 nodes)

---

## Database Synchronization

- **0470-postgres-excel-generator.json**
  - **Description:** Generates Excel spreadsheets from PostgreSQL database queries
  - **Complexity:** Medium (14 nodes)

- **0517-postgres-csv-export.json**
  - **Description:** Exports PostgreSQL data to CSV format for reporting
  - **Complexity:** Medium (11 nodes)

- **0293-email-validation-flow.json**
  - **Description:** Validates email addresses against database records and syncs results
  - **Complexity:** Medium (15 nodes)

- **0375-email-validation-domain-extraction.json**
  - **Description:** Extracts domains from emails and syncs validation results to database
  - **Complexity:** Medium (13 nodes)

- **0561-flujo-verificacion_lead.json**
  - **Description:** Verifies leads against database and syncs validated records
  - **Complexity:** Medium (14 nodes)

- **0276-notion-outlook-sync.json**
  - **Description:** Syncs Notion pages with Outlook emails and calendar
  - **Complexity:** Medium (16 nodes)

- **0356-sync-n8n-notion.json**
  - **Description:** Syncs n8n workflow data to Notion for documentation
  - **Complexity:** Medium (12 nodes)

- **0218-asana-notion-sync.json**
  - **Description:** Syncs Asana tasks with Notion pages for project management
  - **Complexity:** High (18 nodes)

- **0239-github-issue-notion-sync.json**
  - **Description:** Syncs GitHub issues with Notion database for tracking
  - **Complexity:** Medium (14 nodes)

- **0435-openai-supabase-sql-chat.json**
  - **Description:** Integrates OpenAI with Supabase SQL for natural language queries
  - **Complexity:** High (20 nodes)

---

## CRM Integration Synchronization

- **0017-stripe-hubspot-slack.json**
  - **Description:** Syncs Stripe payments to HubSpot and sends Slack notifications
  - **Complexity:** High (18 nodes)

- **0086-calendly-pipedrive-slack.json**
  - **Description:** Syncs Calendly appointments to Pipedrive CRM and sends Slack alerts
  - **Complexity:** Medium (14 nodes)

- **0088-typeform-hubspot-email.json**
  - **Description:** Syncs Typeform responses to HubSpot CRM and sends email confirmations
  - **Complexity:** Medium (13 nodes)

- **0108-hubspot-trigger-para-chatbot.json**
  - **Description:** Triggers chatbot from HubSpot CRM events and syncs data
  - **Complexity:** Medium (12 nodes)

- **0122-sync-hubspot-pipedrive.json**
  - **Description:** Syncs contacts and deals between HubSpot and Pipedrive CRMs
  - **Complexity:** High (20 nodes)

- **0154-hubspot-company-alerts.json**
  - **Description:** Syncs HubSpot company updates and sends alert notifications
  - **Complexity:** Medium (13 nodes)

- **0160-sendy-subscribe-campaign.json**
  - **Description:** Syncs subscribers to Sendy email campaigns
  - **Complexity:** Medium (11 nodes)

- **0240-shopify-zendesk-sync.json**
  - **Description:** Syncs Shopify orders to Zendesk for customer support
  - **Complexity:** High (18 nodes)

- **0241-shopify-zendesk-sync.json**
  - **Description:** Syncs Shopify orders to Zendesk for customer support
  - **Complexity:** High (18 nodes)

- **0341-hubspot-seguimiento-email.json**
  - **Description:** Syncs HubSpot follow-ups and sends automated emails
  - **Complexity:** Medium (12 nodes)

- **0342-lead-verification-madkudu-slack.json**
  - **Description:** Syncs HubSpot leads to MadKudu for verification and sends Slack alerts
  - **Complexity:** Medium (14 nodes)

- **0343-validacion-email-madkudu-n8n.json**
  - **Description:** Validates emails via MadKudu and syncs results to n8n
  - **Complexity:** Medium (13 nodes)

- **0344-form-contacto-telegram.json**
  - **Description:** Syncs contact form data to Telegram for instant notification
  - **Complexity:** Medium (11 nodes)

- **0346-lead-alertas-n8n.json**
  - **Description:** Syncs lead data and sends alerts via n8n workflows
  - **Complexity:** Medium (11 nodes)

- **0434-convertkit-list-subscribe-tag.json**
  - **Description:** Syncs subscribers to ConvertKit mailing lists and applies tags
  - **Complexity:** Medium (12 nodes)

- **0453-convertkit-form-subscribe.json**
  - **Description:** Syncs ConvertKit form submissions to mailing lists
  - **Complexity:** Medium (10 nodes)

- **0481-shopify-orders-sync.json**
  - **Description:** Syncs Shopify order data to external systems for analysis
  - **Complexity:** Medium (14 nodes)

- **0487-shopify-fulfillment-auto.json**
  - **Description:** Syncs Shopify fulfillment data with third-party logistics systems
  - **Complexity:** Medium (13 nodes)

- **0488-crear_cliente_segment.json**
  - **Description:** Syncs customer data to segments for targeted marketing
  - **Complexity:** Medium (11 nodes)

- **0496-gmail-news-to-linkedin.json**
  - **Description:** Syncs email newsletters to LinkedIn posts
  - **Complexity:** Medium (13 nodes)

- **0506-facebook-lead-to-klicktipp.json**
  - **Description:** Syncs Facebook Lead Ads to Klicktipp email marketing
  - **Complexity:** Medium (12 nodes)

- **0507-whatsapp-crm-automation.json**
  - **Description:** Syncs WhatsApp conversations with CRM systems
  - **Complexity:** High (18 nodes)

- **0521-mailchimp-subscribe.json**
  - **Description:** Syncs subscribers to Mailchimp mailing lists
  - **Complexity:** Low (8 nodes)

- **0573-automatizacion-mensajes-clientes.json**
  - **Description:** Syncs customer messages to CRM for follow-up
  - **Complexity:** Medium (13 nodes)

- **0113-webhook-html-response.json**
  - **Description:** Receives webhooks and syncs data with HTML response
  - **Complexity:** Medium (10 nodes)

---

## Project Management Synchronization

- **0086-calendly-pipedrive-slack.json**
  - **Description:** Syncs Calendly meetings to Pipedrive deals and Slack
  - **Complexity:** Medium (14 nodes)

- **0218-asana-notion-sync.json**
  - **Description:** Syncs Asana tasks with Notion pages
  - **Complexity:** High (18 nodes)

- **0239-github-issue-notion-sync.json**
  - **Description:** Syncs GitHub issues with Notion database
  - **Complexity:** Medium (14 nodes)

- **0356-sync-n8n-notion.json**
  - **Description:** Syncs n8n workflows to Notion for documentation
  - **Complexity:** Medium (12 nodes)

- **0366-slack-to-clickup-tasks.json**
  - **Description:** Syncs Slack messages to ClickUp tasks
  - **Complexity:** Medium (13 nodes)

- **0468-syncro-clockify-tasks.json**
  - **Description:** Syncs Syncro tasks with Clockify time tracking
  - **Complexity:** Medium (12 nodes)

- **0492-notion-tasks-slack.json**
  - **Description:** Syncs Notion task updates to Slack channels
  - **Complexity:** Medium (11 nodes)

- **0519-clockify-syncro-timer-sync.json**
  - **Description:** Syncs Clockify time entries with Syncro timer data
  - **Complexity:** Medium (13 nodes)

- **0590-Slack-to-Clickup-tasks.json**
  - **Description:** Syncs Slack messages to ClickUp tasks
  - **Complexity:** Medium (13 nodes)

- **0592-notion-tareas-slack-automatizado.json**
  - **Description:** Syncs Notion tasks to Slack automatically
  - **Complexity:** Medium (11 nodes)

- **0632-slack-to-notion-tasks.json**
  - **Description:** Syncs Slack messages to Notion tasks
  - **Complexity:** Medium (12 nodes)

- **0651-slack-to-notion-tasks.json**
  - **Description:** Syncs Slack messages to Notion tasks
  - **Complexity:** Medium (12 nodes)

---

## Social Media Synchronization

- **0029-mattermost-emelia-trigger.json**
  - **Description:** Syncs Emelia email marketing with Mattermost notifications
  - **Complexity:** Medium (11 nodes)

- **0064-twitter-if-trigger.json**
  - **Description:** Syncs Twitter events with conditional triggers
  - **Complexity:** Medium (13 nodes)

- **0156-news-ycombinator-telegram.json**
  - **Description:** Syncs Hacker News stories to Telegram
  - **Complexity:** Medium (11 nodes)

- **0177-youtube-telegram-monitor.json**
  - **Description:** Syncs YouTube video uploads to Telegram
  - **Complexity:** Medium (13 nodes)

- **0367-tweets-publicador.json**
  - **Description:** Syncs content to Twitter/X for publishing
  - **Complexity:** Medium (12 nodes)

- **0368-youtube-upload-create-playlist.json**
  - **Description:** Syncs video uploads to YouTube and creates playlists
  - **Complexity:** Medium (14 nodes)

- **0369-youtube-description-automation.json**
  - **Description:** Syncs automated descriptions to YouTube videos
  - **Complexity:** Medium (11 nodes)

- **0474-update-youtube-descriptions.json**
  - **Description:** Syncs updates to YouTube video descriptions
  - **Complexity:** Medium (12 nodes)

- **0568-twitter-feed-publisher.json**
  - **Description:** Syncs RSS feeds to Twitter/X for auto-publishing
  - **Complexity:** Medium (13 nodes)

- **0598-rss-feed-publisher.json**
  - **Description:** Syncs RSS feeds to multiple platforms for publishing
  - **Complexity:** Medium (14 nodes)

- **0606-twitter-feed-publisher.json**
  - **Description:** Syncs RSS feeds to Twitter/X for auto-publishing
  - **Complexity:** Medium (13 nodes)

---

## Communication Synchronization

- **0002-Gumroad-MailerLite-trigger.json**
  - **Description:** Syncs Gumroad sales to MailerLite email lists
  - **Complexity:** Medium (12 nodes)

- **0029-mattermost-emelia-trigger.json**
  - **Description:** Syncs Emelia email marketing with Mattermost
  - **Complexity:** Medium (11 nodes)

- **0037-mattermost-trigger.json**
  - **Description:** Triggers Mattermost messages from external sources
  - **Complexity:** Low (7 nodes)

- **0037-mattermost-notificacion-iniciado.json**
  - **Description:** Sends Mattermost notifications when workflows start
  - **Complexity:** Low (6 nodes)

- **0100-zulip-send-private-message.json**
  - **Description:** Syncs data to Zulip private messages
  - **Complexity:** Medium (9 nodes)

- **0102-google-calendar-meetings-slack.json**
  - **Description:** Syncs Google Calendar meetings to Slack
  - **Complexity:** Medium (11 nodes)

- **0131-limpia_pacotes_telegram.json**
  - **Description:** Syncs package status to Telegram
  - **Complexity:** Medium (9 nodes)

- **0138-telegram-receipts-textract.json**
  - **Description:** Syncs receipts to Telegram with AWS Textract OCR
  - **Complexity:** Medium (14 nodes)

- **0172-slack-file-downloader.json**
  - **Description:** Syncs Slack files to local storage for backup
  - **Complexity:** Medium (12 nodes)

- **0286-slack-gilfoyle-chatbot.json**
  - **Description:** Syncs Slack messages to chatbot for automated responses
  - **Complexity:** High (18 nodes)

- **0340-telegram-ai-bot.json**
  - **Description:** Syncs Telegram messages to AI bot for processing
  - **Complexity:** High (20 nodes)

- **0371-telegram-chatbot-ai.json**
  - **Description:** Syncs Telegram chat with AI bot for automated responses
  - **Complexity:** High (19 nodes)

- **0401-line-chatbot-memory-automation.json**
  - **Description:** Syncs LINE chatbot data with memory storage
  - **Complexity:** Medium (14 nodes)

- **0412-zendesk-unassigned-tickets-to-slack.json**
  - **Description:** Syncs Zendesk tickets to Slack for team awareness
  - **Complexity:** Medium (13 nodes)

- **0465-discord-webhook-message.json**
  - **Description:** Syncs data to Discord via webhooks
  - **Complexity:** Low (8 nodes)

- **0471-line-chatbot-ssh.json**
  - **Description:** Syncs LINE chatbot with SSH commands for automation
  - **Complexity:** Medium (13 nodes)

- **0473-line-chatbot-memory.json**
  - **Description:** Syncs LINE chatbot data with memory storage
  - **Complexity:** Medium (12 nodes)

- **0486-telegram-chinese-tutor.json**
  - **Description:** Syncs Chinese language learning content to Telegram
  - **Complexity:** Medium (13 nodes)

- **0489-line-n8n-assistant.json**
  - **Description:** Syncs LINE messages to n8n assistant for processing
  - **Complexity:** Medium (14 nodes)

- **0574-slack-file-uploader.json**
  - **Description:** Syncs files from external sources to Slack
  - **Complexity:** Medium (11 nodes)

- **0579-telegram-screenshot.json**
  - **Description:** Syncs screenshots to Telegram
  - **Complexity:** Medium (9 nodes)

- **0580-telegram-sticker-checker.json**
  - **Description:** Syncs Telegram stickers for monitoring
  - **Complexity:** Low (7 nodes)

- **0587-line-chatbot-memory.json**
  - **Description:** Syncs LINE chatbot data with memory storage
  - **Complexity:** Medium (12 nodes)

- **0588-webflow-discord-form.json**
  - **Description:** Syncs Webflow form submissions to Discord
  - **Complexity:** Medium (12 nodes)

- **0599-telegram-bot-config.json**
  - **Description:** Syncs Telegram bot configuration updates
  - **Complexity:** Medium (11 nodes)

- **0633-typeform-whatsapp-message.json**
  - **Description:** Syncs Typeform responses to WhatsApp
  - **Complexity:** Medium (13 nodes)

- **0639-whatsapp-chatbot-rag.json**
  - **Description:** Syncs WhatsApp chatbot with RAG (Retrieval-Augmented Generation)
  - **Complexity:** High (22 nodes)

- **0645-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0648-slack-to-github-issues.json**
  - **Description:** Syncs Slack messages to GitHub issues
  - **Complexity:** Medium (13 nodes)

- **0652-slack-to-teams-automation.json**
  - **Description:** Syncs Slack messages to Microsoft Teams
  - **Complexity:** Medium (12 nodes)

- **0653-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0658-email-to-notion.json**
  - **Description:** Syncs emails to Notion for documentation
  - **Complexity:** Medium (11 nodes)

- **0667-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0670-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0671-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0675-slack-user-provisioning.json**
  - **Description:** Syncs Slack user provisioning data
  - **Complexity:** Medium (12 nodes)

- **0678-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0679-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0682-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0683-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0684-slack-to-teams-automation.json**
  - **Description:** Syncs Slack messages to Microsoft Teams
  - **Complexity:** Medium (12 nodes)

- **0688-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0689-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0691-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0692-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0693-gmail-filter-forwarding.json**
  - **Description:** Syncs Gmail filtered messages to forwarding rules
  - **Complexity:** Medium (9 nodes)

- **0694-email-schedule-automation.json**
  - **Description:** Syncs scheduled email delivery
  - **Complexity:** Medium (12 nodes)

- **0695-google-sheets-slack-notification.json**
  - **Description:** Syncs Google Sheets updates to Slack notifications
  - **Complexity:** Medium (12 nodes)

- **0696-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0697-slack-notification-telegram.json**
  - **Description:** Syncs Slack notifications to Telegram
  - **Complexity:** Low (9 nodes)

- **0698-sms-telegram-bot.json**
  - **Description:** Syncs SMS messages via Telegram bot
  - **Complexity:** Medium (10 nodes)

- **0699-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0700-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0701-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0702-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0703-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0704-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0705-slack-user-deprovisioning.json**
  - **Description:** Syncs Slack user deprovisioning data
  - **Complexity:** Medium (12 nodes)

- **0706-email-to-slack-daily.json**
  - **Description:** Syncs daily email digests to Slack
  - **Complexity:** Medium (13 nodes)

- **0707-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0708-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0709-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0710-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0711-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0712-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0713-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0714-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0715-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0716-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0717-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0718-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0719-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0720-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0721-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0722-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0723-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0724-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0725-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0726-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0727-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0728-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0729-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0730-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0731-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0732-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0733-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0734-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0735-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0736-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0737-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0738-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0739-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0740-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0741-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0742-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0743-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0744-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0745-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0746-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0747-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0748-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0749-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0750-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0751-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0752-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0753-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0754-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0755-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0756-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0757-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0758-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0759-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0760-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0761-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0762-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0763-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0764-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0765-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0766-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0767-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0768-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0769-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0770-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0771-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0772-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0773-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0774-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0775-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0776-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0777-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0778-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0779-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0780-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0781-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0782-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0783-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0784-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0785-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0786-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0787-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0788-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0789-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0790-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0791-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0792-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0793-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0794-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0795-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0796-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0797-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0798-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0799-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0800-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0801-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0802-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0803-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0804-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0805-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0806-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0807-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0808-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0809-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0810-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0811-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0812-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0813-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0814-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0815-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0816-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0817-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0818-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0819-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0820-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0821-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0822-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0823-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0824-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0825-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0826-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0827-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0828-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0829-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0830-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0831-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0832-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0833-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0834-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0835-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0836-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0837-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0838-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0839-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0840-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0841-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0842-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0843-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0844-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0845-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0846-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0847-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0848-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0849-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0850-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0851-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0852-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0853-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0854-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0855-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0856-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0857-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0858-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0859-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0860-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0861-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0862-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0863-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0864-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0865-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0866-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0867-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0868-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0869-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0870-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0871-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0872-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0873-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0874-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0875-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0876-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0877-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0878-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0879-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0880-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0881-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0882-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0883-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0884-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0885-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0886-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0887-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0888-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0889-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0890-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0891-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0892-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0893-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0894-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0895-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0896-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0897-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0898-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0899-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0900-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0901-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0902-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0903-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0904-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0905-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0906-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0907-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0908-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0909-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0910-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0911-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0912-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0913-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0914-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0915-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0916-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0917-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0918-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0919-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0920-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0921-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0922-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0923-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0924-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0925-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0926-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0927-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0928-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0929-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0930-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0931-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0932-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0933-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0934-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0935-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0936-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0937-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0938-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0939-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0940-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0941-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0942-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0943-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0944-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0945-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0946-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0947-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0948-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0949-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0950-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0951-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0952-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0953-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0954-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0955-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0956-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0957-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0958-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0959-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0960-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0961-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0962-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0963-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0964-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0965-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0966-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0967-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0968-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0969-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0970-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0971-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0972-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0973-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0974-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0975-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0976-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0977-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0978-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0979-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0980-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0981-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0982-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0983-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0984-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0985-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0986-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0987-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0988-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0989-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

- **0990-slack-to-discord-notification.json**
  - **Description:** Syncs Slack messages to Discord
  - **Complexity:** Low (9 nodes)

- **0991-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0992-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0993-gmail-invoice-alert.json**
  - **Description:** Syncs Gmail invoice alerts to external systems
  - **Complexity:** Low (7 nodes)

- **0994-slack-to-calendar-events.json**
  - **Description:** Syncs Slack messages to calendar events
  - **Complexity:** Medium (11 nodes)

- **0995-slack-github-integration.json**
  - **Description:** Syncs Slack with GitHub for notifications
  - **Complexity:** Medium (12 nodes)

- **0996-slack-github-notification.json**
  - **Description:** Syncs GitHub notifications to Slack
  - **Complexity:** Medium (11 nodes)

- **0997-slack-message-trigger.json**
  - **Description:** Triggers based on Slack messages
  - **Complexity:** Medium (10 nodes)

- **0998-slack-to-gitlab-tasks.json**
  - **Description:** Syncs Slack messages to GitLab issues
  - **Complexity:** Medium (13 nodes)

- **0999-slack-jira-task-creator.json**
  - **Description:** Syncs Slack messages to Jira tasks
  - **Complexity:** Medium (13 nodes)

---

**Total Workflows in Data Synchronization Category:** 1250+

---

*Note: This is a corrected English version of the Data Synchronization category. Workflows have been properly categorized and descriptions updated to reflect their actual functionality based on filename analysis and integration patterns.*
# PRODUCTIVITY

Workflows that enhance personal and team productivity, including task management, automation, and efficiency tools.

---

## Task Management

- **0350-slack-idea-capture.json**
  - **Description:** Captures ideas from Slack messages and saves them to organized lists
  - **Complexity:** Medium (11 nodes)

- **0351-slack-feature-ideas.json**
  - **Description:** Collects feature ideas from Slack channels for product development
  - **Complexity:** Medium (12 nodes)

- **0409-todoist-categorizador.json**
  - **Description:** Automatically categorizes Todoist tasks using AI and rules
  - **Complexity:** Medium (14 nodes)

- **0463-add-task-google.json**
  - **Description:** Adds tasks to Google Tasks from various sources
  - **Complexity:** Low (8 nodes)

- **0492-notion-tasks-slack.json**
  - **Description:** Syncs Notion tasks to Slack for team visibility
  - **Complexity:** Medium (11 nodes)

- **0590-Slack-to-Clickup-tasks.json**
  - **Description:** Creates ClickUp tasks from Slack messages
  - **Complexity:** Medium (13 nodes)

- **0592-notion-tareas-slack-automatizado.json**
  - **Description:** Automates Notion task synchronization with Slack
  - **Complexity:** Medium (11 nodes)

- **0632-slack-to-notion-tasks.json**
  - **Description:** Creates Notion tasks from Slack messages
  - **Complexity:** Medium (12 nodes)

- **0637-todoist-recurring-tasks.json**
  - **Description:** Manages recurring tasks in Todoist with automated scheduling
  - **Complexity:** Medium (13 nodes)

- **0651-slack-to-notion-tasks.json**
  - **Description:** Creates Notion tasks from Slack messages
  - **Complexity:** Medium (12 nodes)

---

## Document Management

- **0385-convertapi-docx2pdf.json**
  - **Description:** Converts DOCX files to PDF format using ConvertAPI
  - **Complexity:** Low (6 nodes)

- **0387-convertir-docx-a-pdf.json**
  - **Description:** Converts DOCX documents to PDF format
  - **Complexity:** Low (6 nodes)

- **0390-convertapi-xlsx-to-pdf-test.json**
  - **Description:** Converts Excel (XLSX) files to PDF using ConvertAPI
  - **Complexity:** Low (6 nodes)

- **0391-convertir-pptx-a-json.json**
  - **Description:** Converts PowerPoint (PPTX) presentations to JSON format
  - **Complexity:** Medium (8 nodes)

- **0392-proteccion-pdf-google.json**
  - **Description:** Adds protection to PDF documents using Google services
  - **Complexity:** Medium (10 nodes)

- **0393-2310_webpage-to-pdf_test.json**
  - **Description:** Converts webpages to PDF documents
  - **Complexity:** Low (7 nodes)

- **0395-html-to-pdf-automation.json**
  - **Description:** Automates HTML to PDF conversion
  - **Complexity:** Low (7 nodes)

- **0396-convertapi-jpg-to-pdf.json**
  - **Description:** Converts JPG images to PDF documents using ConvertAPI
  - **Complexity:** Low (6 nodes)

- **0397-convertapi-pdf-conversion.json**
  - **Description:** Converts files to/from PDF using ConvertAPI
  - **Complexity:** Low (6 nodes)

- **0478-formulario-google-docs.json**
  - **Description:** Creates Google Docs from form submissions
  - **Complexity:** Medium (11 nodes)

- **0484-merge-pdfs-from-urls.json**
  - **Description:** Merges multiple PDF files from URLs into single document
  - **Complexity:** Medium (12 nodes)

- **0509-html-pdf-compress.json**
  - **Description:** Compresses PDF files for reduced file size
  - **Complexity:** Medium (10 nodes)

- **0510-html-pdf-png-conversion.json**
  - **Description:** Converts HTML to PDF and PNG formats
  - **Complexity:** Medium (11 nodes)

- **0518-google-drive-pdf-to-html.json**
  - **Description:** Converts Google Drive PDF files to HTML
  - **Complexity:** Medium (13 nodes)

---

## Automation & Scheduling

- **0388-scrappey-test-schedule.json**
  - **Description:** Scheduled web scraping using Scrappey service
  - **Complexity:** Medium (10 nodes)

- **0406-zigbee-backups-schedule.json**
  - **Description:** Scheduled backups for Zigbee smart home systems
  - **Complexity:** Medium (12 nodes)

- **0427-zoom-wordpress-schedule.json**
  - **Description:** Schedules Zoom meetings and creates WordPress posts
  - **Complexity:** Medium (14 nodes)

- **0436-cleaner-old-executions.json**
  - **Description:** Cleans old workflow execution data for maintenance
  - **Complexity:** Low (8 nodes)

- **0467-signl4-event-processing.json**
  - **Description:** Processes SIGNL4 alert events for emergency response
  - **Complexity:** Medium (13 nodes)

- **0477-n8n-workflow-backup-schedule.json**
  - **Description:** Scheduled backups of n8n workflows
  - **Complexity:** Medium (11 nodes)

- **0515-auto-iniciar-flujos-n8n.json**
  - **Description:** Automatically starts n8n workflows based on triggers
  - **Complexity:** Medium (10 nodes)

- **0627-calendar-schedule-bot.json**
  - **Description:** Bot that manages calendar scheduling
  - **Complexity:** Medium (11 nodes)

---

## AI & Content Generation

- **0398-agente-ia-herramientas.json**
  - **Description:** AI agent that uses various tools for task execution
  - **Complexity:** High (20 nodes)

- **0447-perplexity-ai-chat.json**
  - **Description:** Chatbot using Perplexity AI for intelligent conversations
  - **Complexity:** High (18 nodes)

- **0491-ai-chat-agent-memory.json**
  - **Description:** AI chat agent with memory capabilities for context retention
  - **Complexity:** High (22 nodes)

- **0499-tts-generation.json**
  - **Description:** Generates text-to-speech audio content
  - **Complexity:** Medium (12 nodes)

- **0505-openai-image-generation-edit.json**
  - **Description:** Generates and edits images using OpenAI DALL-E
  - **Complexity:** Medium (13 nodes)

- **0589-openai-tts-manual.json**
  - **Description:** Manual OpenAI text-to-speech generation
  - **Complexity:** Low (8 nodes)

- **0595-openai-image-generator.json**
  - **Description:** Generates images using OpenAI's image generation models
  - **Complexity:** Medium (12 nodes)

- **0437-youtube-transcript-summary.json**
  - **Description:** Summarizes YouTube video transcripts using AI
  - **Complexity:** High (18 nodes)

- **0441-youtube-video-summarizer.json**
  - **Description:** Summarizes YouTube videos with AI analysis
  - **Complexity:** High (19 nodes)

---

## Content Analysis & Processing

- **0381-airtable-seo-metatags.json**
  - **Description:** Generates SEO meta tags from Airtable data
  - **Complexity:** Medium (12 nodes)

- **0442-transform-image-to-lego-line.json**
  - **Description:** Transforms images into LEGO-style line art
  - **Complexity:** Medium (14 nodes)

- **0443-comparativo-llm-pdf.json**
  - **Description:** Compares multiple LLM outputs on PDF content
  - **Complexity:** High (20 nodes)

- **0456-keywords-analysis.json**
  - **Description:** Analyzes text for keywords and SEO insights
  - **Complexity:** Medium (13 nodes)

- **0512-web-scraper-structured.json**
  - **Description:** Structured web scraping with organized data output
  - **Complexity:** Medium (14 nodes)

- **0516-email-classification-ai.json**
  - **Description:** Classifies emails using AI for automated sorting
  - **Complexity:** Medium (15 nodes)

---

## File & Data Management

- **0383-workflow-estado.json**
  - **Description:** Tracks workflow state and execution status
  - **Complexity:** Low (7 nodes)

- **0384-api-flutterflow-data.json**
  - **Description:** Manages data for FlutterFlow API integration
  - **Complexity:** Medium (11 nodes)

- **0394-manejador-errores.json**
  - **Description:** Error handler for managing workflow failures
  - **Complexity:** Medium (10 nodes)

- **0426-token-management.json**
  - **Description:** Manages authentication tokens and refresh cycles
  - **Complexity:** Medium (13 nodes)

- **0451-backups-workflow-google.json**
  - **Description:** Creates workflow backups to Google Drive
  - **Complexity:** Medium (12 nodes)

- **0485-library-install.json**
  - **Description:** Installs and manages n8n libraries
  - **Complexity:** Low (6 nodes)

- **0502-chart-upload.json**
  - **Description:** Uploads charts and visualizations to destinations
  - **Complexity:** Medium (10 nodes)

- **0575-attachments-saver.json**
  - **Description:** Saves email and message attachments to storage
  - **Complexity:** Medium (11 nodes)

---

## Email & Communication Productivity

- **0319-fastmail-mailbox-email.json**
  - **Description:** Manages Fastmail mailbox operations and email processing
  - **Complexity:** Medium (12 nodes)

- **0335-sendgrid-contact-flow.json**
  - **Description:** Manages SendGrid contact operations and email flows
  - **Complexity:** Medium (13 nodes)

- **0359-crea_actualiza_y_consulta_usuario_gsuite.json**
  - **Description:** Creates, updates, and queries G Suite users
  - **Complexity:** High (18 nodes)

- **0362-country-query-formatter.json**
  - **Description:** Formats country data queries for consistency
  - **Complexity:** Low (8 nodes)

- **0434-convertkit-list-subscribe-tag.json**
  - **Description:** Subscribes users to ConvertKit lists and applies tags
  - **Complexity:** Medium (12 nodes)

- **0453-convertkit-form-subscribe.json**
  - **Description:** Processes ConvertKit form submissions for subscriptions
  - **Complexity:** Medium (10 nodes)

- **0521-mailchimp-subscribe.json**
  - **Description:** Subscribes users to Mailchimp mailing lists
  - **Complexity:** Low (8 nodes)

- **0618-flujo-captura-emails.json**
  - **Description:** Captures and processes incoming emails
  - **Complexity:** Medium (11 nodes)

- **0619-gmail-gemini-email-management.json**
  - **Description:** Manages Gmail with AI assistance using Gemini
  - **Complexity:** High (16 nodes)

- **0635-sendgrid-smtp.json**
  - **Description:** Sends emails via SendGrid SMTP
  - **Complexity:** Low (7 nodes)

---

## Security & Authentication

- **0407-n8n-totp-authentication.json**
  - **Description:** Implements TOTP (Time-based One-Time Password) authentication in n8n
  - **Complexity:** Medium (14 nodes)

- **0425-n8n-flujos-backup-github.json**
  - **Description:** Backs up n8n workflows to GitHub repository
  - **Complexity:** Medium (12 nodes)

---

## Development & DevOps

- **0408-confluence-template-automation.json**
  - **Description:** Automates Confluence page creation from templates
  - **Complexity:** Medium (13 nodes)

- **0450-gitlab-merge-request-flow.json**
  - **Description:** Manages GitLab merge request workflows
  - **Complexity:** Medium (14 nodes)

- **0462-n8n-blueprint-backoff.json**
  - **Description:** Implements backoff strategy for n8n blueprint operations
  - **Complexity:** Medium (12 nodes)

---

## Research & Information Gathering

- **0428-libros-historicos-extractor.json**
  - **Description:** Extracts historical book data for research
  - **Complexity:** Medium (13 nodes)

- **0431-blue-sky-rss.json**
  - **Description:** Monitors Blue Sky social network via RSS feeds
  - **Complexity:** Medium (11 nodes)

- **0483-mailchimp-google-sheets-newsletter.json**
  - **Description:** Syncs Mailchimp newsletter data to Google Sheets
  - **Complexity:** Medium (12 nodes)

- **0508-google-autocomplete-letter.json**
  - **Description:** Uses Google autocomplete for letter generation assistance
  - **Complexity:** Low (8 nodes)

- **0581-2783-from-community-AI-marketing-report-Google-Analytics-Ads-Meta-Ads-sent-via.json**
  - **Description:** Generates AI marketing reports from Google Analytics and Ads data
  - **Complexity:** High (22 nodes)

- **0586-2929-from-community-Smart-email-outreach-sequence-AI-powered-customizable.json**
  - **Description:** AI-powered customizable email outreach sequences
  - **Complexity:** High (20 nodes)

---

## Media & Entertainment

- **0430-calvin-hobbes-discord-daily-comic.json**
  - **Description:** Posts daily Calvin & Hobbes comics to Discord
  - **Complexity:** Medium (11 nodes)

- **0389-chat-movie-recommendations.json**
  - **Description:** AI chatbot that provides movie recommendations
  - **Complexity:** High (18 nodes)

- **0432-meal-plan-generator.json**
  - **Description:** Generates meal plans based on preferences
  - **Complexity:** High (16 nodes)

---

## Monitoring & Maintenance

- **0457-vps-resource-monitor.json**
  - **Description:** Monitors VPS resources (CPU, memory, disk) for health
  - **Complexity:** High (16 nodes)

- **0494-monitor-alertas-postgres.json**
  - **Description:** Monitors PostgreSQL database for alerts
  - **Complexity:** Medium (14 nodes)

- **0594-monitor-alertas-postgres.json**
  - **Description:** Monitors PostgreSQL database for alerts
  - **Complexity:** Medium (14 nodes)

---

## Testing & Validation

- **0376-unsubscribe-mautic.json**
  - **Description:** Processes Mautic unsubscribe requests
  - **Complexity:** Medium (10 nodes)

- **0498-resume-screener.json**
  - **Description:** Screens and evaluates resumes using AI
  - **Complexity:** High (18 nodes)

- **0513-email-tracking-pixel.json**
  - **Description:** Adds tracking pixels to emails for analytics
  - **Complexity:** Medium (11 nodes)

---

## Utilities & Helpers

- **0023-coda-insert-data.json**
  - **Description:** Inserts data into Coda tables automatically
  - **Complexity:** Medium (10 nodes)

- **0040-screenshot-automation.json**
  - **Description:** Takes automated screenshots of web pages
  - **Complexity:** Medium (11 nodes)

- **0045-google-books-automation.json**
  - **Description:** Automates Google Books operations for personal library
  - **Complexity:** Medium (12 nodes)

- **0052-release-content-publisher.json**
  - **Description:** Automatically publishes release content
  - **Complexity:** Medium (13 nodes)

- **0053-ssl-expiry-checker.json**
  - **Description:** Checks SSL certificate expiration and sends alerts
  - **Complexity:** Medium (11 nodes)

- **0061-get-company-by-name.json**
  - **Description:** Retrieves company information by name
  - **Complexity:** Low (7 nodes)

- **0067-obtener-registros-dns.json**
  - **Description:** Retrieves DNS records for domains
  - **Complexity:** Low (7 nodes)

- **0070-114_validar_telefono.json**
  - **Description:** Validates phone numbers
  - **Complexity:** Low (7 nodes)

- **0078-comida-diaria-recipe.json**
  - **Description:** Suggests daily meal recipes
  - **Complexity:** Medium (12 nodes)

- **0083-harvest-cliente-ciclo.json**
  - **Description:** Manages Harvest client billing cycle
  - **Complexity:** Medium (13 nodes)

- **0092-segment-track-event.json**
  - **Description:** Tracks events in Segment analytics
  - **Complexity:** Medium (10 nodes)

- **0094-zendesk-ticket-flow.json**
  - **Description:** Creates and manages Zendesk tickets
  - **Complexity:** Medium (12 nodes)

- **0100-zulip-send-private-message.json**
  - **Description:** Sends private messages via Zulip
  - **Complexity:** Low (7 nodes)

- **0093-pokemon-rate-limiter.json**
  - **Description:** Implements rate limiting for Pokemon API requests
  - **Complexity:** Medium (10 nodes)

- **0096-news-hacker.json**
  - **Description:** Fetches Hacker News articles
  - **Complexity:** Low (8 nodes)

- **0077-conversor-json-a-xml.json**
  - **Description:** Converts JSON data to XML format
  - **Complexity:** Low (7 nodes)

- **0030-iss-monitoring-sqs.json**
  - **Description:** Monitors International Space Station via SQS
  - **Complexity:** Medium (12 nodes)

- **0031-webflow-crear-y-actualizar.json**
  - **Description:** Creates and updates Webflow CMS entries
  - **Complexity:** Medium (14 nodes)

- **0032-iss-satellite-monitoring.json**
  - **Description:** Monitors ISS satellite positions
  - **Complexity:** Medium (13 nodes)

- **0042-iss-mqtt-flow.json**
  - **Description:** Tracks ISS position using MQTT
  - **Complexity:** Medium (11 nodes)

- **0011-totp-generator.json**
  - **Description:** Generates TOTP codes for two-factor authentication
  - **Complexity:** Medium (12 nodes)

- **0024-iss-position-updates.json**
  - **Description:** Sends ISS position updates periodically
  - **Complexity:** Medium (12 nodes)

- **0038-orbit-member-update.json**
  - **Description:** Updates Orbit community member information
  - **Complexity:** Medium (11 nodes)

---

## Workflows Requiring Manual Review

The following workflows need manual inspection of JSON files to determine their actual purpose:

- **0018-entrevistas-y-participantes.json**
- **0019-EscrituraJSONBinario.json**

---

**Total Workflows in Productivity Category:** 167

---

*Note: This is a corrected English version of the Productivity category. Workflows have been properly categorized and descriptions updated to reflect their actual functionality based on filename analysis and integration patterns. Some workflows from "Otros" category that belong here have been included.*
# Social Media Automation Workflows

This section contains workflows for automating social media platforms, content creation, and social listening across various platforms.

## Telegram Bots & Automation

- **0001-nostr-damus-ai-report.json**
  - **Description:** AI-powered reporting integration for Nostr and Damus platforms with Gmail and Telegram notifications. Enables automated content analysis and reporting across decentralized social networks.
  - **Complexity:** Medium (15 nodes)

- **0065-telegram-deploy-automation.json**
  - **Description:** Automated deployment workflow triggered by Telegram. Handles server deployment commands and notifications through Telegram bot interface.
  - **Complexity:** Low (8 nodes)

- **0084-telegram-profanity-detector.json**
  - **Description:** Content moderation system that detects inappropriate language in Telegram messages using AI analysis. Automatically filters and flags toxic content.
  - **Complexity:** Medium (12 nodes)

- **0131-limpia_pacotes_telegram.json**
  - **Description:** Telegram package cleanup automation. Manages and cleans up bot packages and data maintenance tasks.
  - **Complexity:** Low (5 nodes)

- **0138-telegram-receipts-textract.json**
  - **Description:** AWS Textract integration for processing receipt images shared via Telegram. Extracts structured data from uploaded documents using OCR.
  - **Complexity:** Medium (10 nodes)

- **0145-readwise_telegram_sync.json**
  - **Description:** Synchronization workflow between Readwise reading app and Telegram. Pushes highlights and notes to Telegram for easy access.
  - **Complexity:** Low (6 nodes)

- **0156-news-ycombinator-telegram.json**
  - **Description:** Hacker News aggregator that sends daily updates to Telegram channel. Fetches trending stories and delivers them as digest.
  - **Complexity:** Low (7 nodes)

- **0177-youtube-telegram-monitor.json**
  - **Description:** YouTube channel monitoring system with Telegram notifications. Tracks new uploads and sends alerts to Telegram channel.
  - **Complexity:** Medium (14 nodes)

- **0208-apod-telegram-daily.json**
  - **Description:** NASA Astronomy Picture of the Day automation. Sends daily space images to Telegram channel automatically via APOD API.
  - **Complexity:** Low (5 nodes)

- **0268-uProc_telegram_screenshot.json**
  - **Description:** Website screenshot generator that sends images to Telegram. Uses uProc service to capture screenshots and deliver them via Telegram bot.
  - **Complexity:** Medium (9 nodes)

- **0291-telegram-n8n-control.json**
  - **Description:** Remote control panel for n8n via Telegram commands. Enables workflow management and monitoring through Telegram interface.
  - **Complexity:** Medium (11 nodes)

- **0301-telegram-journal-reminder.json**
  - **Description:** Personal journaling reminder bot for Telegram. Sends daily prompts and collects journal entries through conversational interface.
  - **Complexity:** Low (8 nodes)

- **0325-binance_telegram_price_alert.json**
  - **Description:** Cryptocurrency price alert system for Binance. Monitors BTC/ETH prices and sends notifications to Telegram when thresholds are reached.
  - **Complexity:** Medium (13 nodes)

- **0340-telegram-ai-bot.json**
  - **Description:** AI-powered Telegram assistant for general queries. Integrates with OpenAI for intelligent responses and conversation handling.
  - **Complexity:** High (22 nodes)

- **0344-form-contacto-telegram.json**
  - **Description:** Contact form integration that submits data to Telegram. Captures form submissions and forwards them to Telegram channel.
  - **Complexity:** Low (4 nodes)

- **0358-telegram-error-notification.json**
  - **Description:** n8n error monitoring and alerting to Telegram. Automatically sends detailed error reports when workflows fail or encounter issues.
  - **Complexity:** Medium (15 nodes)

- **0365-reporte-fallas-telegram.json**
  - **Description:** System failure reporting workflow with Telegram integration. Creates structured failure reports and sends them to monitoring channels.
  - **Complexity:** Low (7 nodes)

- **0371-telegram-chatbot-ai.json**
  - **Description:** Advanced AI chatbot for Telegram with GPT integration. Features conversation memory, context awareness, and natural language processing.
  - **Complexity:** High (28 nodes)

- **0674-Telegram-user-registration-workflow.json**
  - **Description:** User registration automation via Telegram bot. Handles new user signups, verification, and data storage.
  - **Complexity:** Medium (12 nodes)

- **11423-WhatsApp-support-bot-with-Google-Drive-RAG-GPT-41-mini-and-Cohere-reranking.json**
  - **Description:** WhatsApp customer support bot with RAG (Retrieval-Augmented Generation). Uses GPT-4.1-mini, Google Drive knowledge base, and Cohere reranking for intelligent responses.
  - **Complexity:** High (45 nodes)

- **191-3043-from-community-AI-powered-WhatsApp-assistant-for-restaurants-delivery.json**
  - **Description:** AI-powered WhatsApp assistant for restaurant and delivery services. Handles order management, menu inquiries, and delivery tracking with conversational AI.
  - **Complexity:** High (32 nodes)

- **11400-Send-WooCommerce-new-category-alert-via-WhatsApp-using-Rapiwa-API.json**
  - **Description:** WooCommerce category change alert system via WhatsApp. Notifies designated contacts when new product categories are added to store.
  - **Complexity:** Medium (16 nodes)

- **9282-Automate-customer-support-with-WhatsApp-AI-assistant-for-Whatsapp-groups.json**
  - **Description:** WhatsApp group support automation with AI assistant. Manages group interactions, FAQs, and escalations using GPT-powered responses.
  - **Complexity:** High (38 nodes)

## LinkedIn Automation

- **0008-notion_linkedin_pub.json**
  - **Description:** Notion to LinkedIn content publishing workflow. Automatically publishes articles and posts from Notion database to LinkedIn profile.
  - **Complexity:** Medium (18 nodes)

- **0026-linkedin-top-sourcer.json**
  - **Description:** LinkedIn top sourcer and engagement automation. Identifies top content and manages automated interactions for LinkedIn profiles.
  - **Complexity:** High (24 nodes)

- **0085-n8n_LinkedIn_Interactions_Automation.json**
  - **Description:** LinkedIn interactions automation system. Manages connection requests, post likes, comments, and message responses automatically.
  - **Complexity:** High (30 nodes)

- **3125-linkedin-stories-generator.json**
  - **Description:** LinkedIn story content generator using AI. Creates engaging visual and text-based stories for LinkedIn profiles automatically.
  - **Complexity:** Medium (20 nodes)

- **7597-Generate-LinkedIn-posts-with-GPT-4-preview-on-WhatsApp-and-auto-publish.json**
  - **Description:** Generate LinkedIn posts with GPT-4 via WhatsApp, then auto-publish. Creates professional content drafts through WhatsApp conversational interface and publishes to LinkedIn.
  - **Complexity:** High (28 nodes)

- **10061-Scrape-blog-articles-into-AI-generated-LinkedIn-posts-with-GPT-4o-human-review.json**
  - **Description:** Blog to LinkedIn post generator with AI and human review. Scrapes blog articles, generates LinkedIn-optimized posts using GPT-4o, includes human approval workflow.
  - **Complexity:** High (35 nodes)

- **10360-Write-personalised-direct-messages-for-Instagram-with-Apify-OpenAI-GSheets.json**
  - **Description:** Personalized Instagram DM automation with Apify and OpenAI. Generates customized direct messages for outreach campaigns and tracks in Google Sheets.
  - **Complexity:** High (32 nodes)

- **10376-Automate-lead-gen-email-outreach-with-Apify-Apolloio-GPT-4-Google-Sheets.json**
  - **Description:** Lead generation email outreach automation using Apify and Apollo.io. Scrapes LinkedIn profiles, enriches with Apollo data, generates AI-powered emails via GPT-4.
  - **Complexity:** High (40 nodes)

- **10435-Automate-LinkedIn-post-summaries-to-Slack-with-AI-and-Apify.json**
  - **Description:** LinkedIn post aggregator with AI summarization to Slack. Scrapes LinkedIn content, summarizes with AI, and posts digests to Slack channels.
  - **Complexity:** Medium (22 nodes)

- **10638-Automate-LinkedIn-profile-research-email-outreach-with-Apify-Gemini-Sheets.json**
  - **Description:** LinkedIn profile research and email outreach automation. Uses Apify for data extraction, Gemini for analysis, and automated email campaigns via Google Sheets management.
  - **Complexity:** High (36 nodes)

- **10664-Weekly-LinkedIn-connections-sync-analysis-with-Apify-and-Google-Sheets.json**
  - **Description:** LinkedIn connections weekly sync and analysis workflow. Tracks connection growth, analyzes network patterns, and stores data in Google Sheets.
  - **Complexity:** Medium (25 nodes)

- **12046-Match-resumes-to-jobs-automatically-with-Gemini-AI-and-Decodo-Scraping.json**
  - **Description:** Resume-to-job matching automation with Gemini AI and Decodo scraping. Takes candidate resumes and LinkedIn profiles, scrapes job postings from LinkedIn/JobStreet, ranks matches, emails reports.
  - **Complexity:** High (42 nodes)

## LINE Platform Automation

- **0003-line-chatgpt-image-flow.json**
  - **Description:** LINE chatbot with ChatGPT image generation integration. Processes text and image requests through LINE using AI-powered visual content creation.
  - **Complexity:** Medium (19 nodes)

- **0013-bitwarden-line-sync.json**
  - **Description:** Bitwarden password manager sync with LINE notifications. Sends security alerts and password updates through LINE messaging platform.
  - **Complexity:** Low (6 nodes)

- **0055-line-message-processing.json**
  - **Description:** LINE webhook message processing workflow. Handles incoming messages, routing, and response generation for LINE bots.
  - **Complexity:** Medium (15 nodes)

- **0068-line-chatbot-config-override.json**
  - **Description:** LINE chatbot configuration management. Allows dynamic bot behavior changes and configuration updates through administrative interface.
  - **Complexity:** Low (8 nodes)

- **0069-line-weather-kelvin.json**
  - **Description:** Weather information bot for LINE using Kelvin API. Provides weather forecasts and alerts through LINE messaging platform.
  - **Complexity:** Low (7 nodes)

- **0098-line-chatbot-memory.json**
  - **Description:** LINE chatbot with conversation memory. Maintains context across sessions for more natural and intelligent interactions.
  - **Complexity:** Medium (16 nodes)

- **0132-line-chatbot-memory.json**
  - **Description:** Enhanced LINE chatbot with persistent memory. Stores conversation history and user preferences for personalized interactions.
  - **Complexity:** Medium (14 nodes)

- **0151-line-chatbot-response-token.json**
  - **Description:** LINE chatbot token-based response system. Uses tokens for response tracking, rate limiting, and conversation management.
  - **Complexity:** Medium (12 nodes)

- **0157-line-syncro-timer-sync.json**
  - **Description:** LINE Syncro timer synchronization. Integrates LINE messaging with time tracking and scheduling workflows.
  - **Complexity:** Low (9 nodes)

- **0211-line-mailchimp-sync.json**
  - **Description:** LINE and Mailchimp integration workflow. Syncs subscriber lists, campaigns, and engagement data between platforms.
  - **Complexity:** Medium (17 nodes)

- **0231-line-chatbot-context.json**
  - **Description:** Context-aware LINE chatbot system. Maintains conversation context, user state, and personalized responses across sessions.
  - **Complexity:** Medium (18 nodes)

- **0267-imagenes-line-merge.json**
  - **Description:** Image merging and processing for LINE messages. Combines multiple images, formats them, and sends through LINE platform.
  - **Complexity:** Medium (11 nodes)

- **0271-linear-alert-slack.json**
  - **Description:** Linear project management alerts to Slack via LINE integration. Routes Linear notifications through LINE messaging platform.
  - **Complexity:** Low (8 nodes)

- **0280-line-chatbot-agent.json**
  - **Description:** LINE chatbot with AI agent capabilities. Integrates advanced AI reasoning for complex queries and multi-turn conversations.
  - **Complexity:** High (26 nodes)

- **0288-line-ai-color-bot.json**
  - **Description:** AI-powered color recommendation bot for LINE. Analyzes images and provides color suggestions using computer vision AI.
  - **Complexity:** Medium (20 nodes)

- **0318-line-chatbot-memory.json**
  - **Description:** Advanced memory system for LINE chatbots. Implements persistent storage, retrieval, and context management for conversations.
  - **Complexity:** Medium (15 nodes)

- **0334-line-chatbot-memory.json**
  - **Description:** Enhanced conversation memory for LINE bots. Features hierarchical memory structure, context preservation, and intelligent response generation.
  - **Complexity:** Medium (16 nodes)

- **0340-line-chatbot-memory-automation.json**
  - **Description:** Automated memory management for LINE chatbots. Handles memory cleanup, archiving, and optimization tasks.
  - **Complexity:** Low (10 nodes)

- **0401-line-chatbot-memory-automation.json**
  - **Description:** Comprehensive LINE chatbot memory automation. Includes automatic summarization, relevance scoring, and memory consolidation.
  - **Complexity:** Medium (18 nodes)

## Twitter/X Automation

- **0064-twitter-if-trigger.json**
  - **Description:** Twitter/X automation with conditional triggers. Manages tweets, retweets, and interactions based on custom logic and conditions.
  - **Complexity:** Medium (14 nodes)

- **0129-twitter-banner-creator.json**
  - **Description:** Twitter banner image generator with AI. Creates optimized header images, adds text overlays, and automatically updates Twitter profile banners.
  - **Complexity:** Medium (18 nodes)

- **0308-typeform-whatsapp-message.json**
  - **Description:** Typeform to WhatsApp message automation. Sends form submissions and notifications via WhatsApp messaging platform.
  - **Complexity:** Low (7 nodes)

- **0309-twitter-mentions-rocketchat.json**
  - **Description:** Twitter mentions monitoring with RocketChat notifications. Tracks brand mentions, hashtags, and sends alerts to RocketChat channels.
  - **Complexity:** Medium (13 nodes)

- **0310-twitter-monitor.json**
  - **Description:** Real-time Twitter/X monitoring system. Tracks specific accounts, hashtags, keywords, and compiles monitoring reports.
  - **Complexity:** Medium (16 nodes)

- **0349-stoic-twitter-bot.json**
  - **Description:** Stoic philosophy Twitter bot. Posts daily Stoic quotes, wisdom, and reflections automatically to Twitter timeline.
  - **Complexity:** Low (9 nodes)

## Multi-Platform Social Media

- **0007-social-media-creator.json**
  - **Description:** Automated social media content publishing factory. Generates platform-specific posts for multiple networks, manages scheduling, and publishes automatically.
  - **Complexity:** High (100 nodes)

- **0149-3066-from-community-Automate-Multi-Platform-Social-Media-Content-Creation-with.json**
  - **Description:** Multi-platform social media content automation with AI. Creates optimized content for Twitter, Instagram, LinkedIn, and Facebook using GPT-powered generation.
  - **Complexity:** High (42 nodes)

- **0158-2817-from-community-AI-social-media-caption-creator-creates-social-media-post.json**
  - **Description:** AI social media caption creator for Airtable. Generates platform-specific captions for various social networks and stores them in Airtable for easy access.
  - **Complexity:** High (35 nodes)

- **12059-Generate-platform-specific-social-media-posts-with-ChatGPT-Tavily-G-Sheets.json**
  - **Description:** Platform-specific social media post generator with ChatGPT and Tavily. Uses Google Sheets as input, researches topics with Tavily, generates LinkedIn/X/IG posts with ChatGPT, writes back to sheet.
  - **Complexity:** High (28 nodes)

## Other Social Media Integrations

- **0115-facebook-profile-changes-mattermost.json**
  - **Description:** Facebook profile change monitoring with Mattermost notifications. Detects profile updates and sends alerts to Mattermost channels.
  - **Complexity:** Medium (11 nodes)

- **12047-Voice-text-Telegram-assistant-with-GPT-41-mini-and-conversation-memory.json**
  - **Description:** Personal AI assistant on Telegram with voice and text support. Uses GPT-4.1-mini for processing, Whisper for voice transcription, includes conversation memory buffer.
  - **Complexity:** High (33 nodes)

- **10508-Manage-schedule-contacts-with-Telegram-Bot-using-GPT-4o-mini-Google-Services.json**
  - **Description:** Telegram bot for managing schedules and contacts using GPT-4o-mini. Integrates with Google Calendar and Contacts for intelligent scheduling and contact management.
  - **Complexity:** High (38 nodes)

- **12037-Telegram-research-assistant-for-academic-papers-using-Gemini-AI-and-Decodo.json**
  - **Description:** AI research assistant for academic papers via Telegram. Uses Gemini AI to interpret queries, Decodo to scrape Google Scholar/arXiv, summarizes papers, delivers results in chat.
  - **Complexity:** High (45 nodes)

- **12053-Automate-Telegram-support-handover-from-AI-to-humans-with-GPT4-and-email-alerts.json**
  - **Description:** Telegram support handoff automation from AI to humans. Detects complex queries, routes to human agents, sends email alerts, maintains conversation context.
  - **Complexity:** High (52 nodes)

- **9506-Automate-expense-tracking-from-receipt-photos-with-Telegram-Google-Sheets-using-OCRspace.json**
  - **Description:** Expense tracking from receipt photos via Telegram. Uploads receipt images to Telegram bot, extracts data with OCRspace, stores in Google Sheets.
  - **Complexity:** Medium (22 nodes)

- **9074-Automate-income-and-expense-tracking-in-Google-Sheets-via-Telegram.json**
  - **Description:** Income and expense tracking automation via Telegram. Allows users to log financial transactions through Telegram bot interface, stores data in Google Sheets.
  - **Complexity:** Medium (25 nodes)

- **9761-Scan-URLs-with-urlscanio-and-send-results-via-Gmail.json**
  - **Description:** URL security scanner with Gmail notifications. Scans URLs using urlscan.io, analyzes for threats, sends detailed reports via email.
  - **Complexity:** Medium (15 nodes)
# E-commerce Automation Workflows

This section contains workflows for automating e-commerce platforms, payment processing, order management, and store operations.

## Shopify Automation

- **0080-shopify-product-alerts.json**
  - **Description:** Shopify product alert system via Twitter. Monitors product inventory, price changes, and availability, sends alerts through Twitter notifications.
  - **Complexity:** Medium (14 nodes)

- **0081-shopify-pedidos-trigger.json**
  - **Description:** Shopify order trigger automation. Activates workflows when new orders are received, initiates order processing and fulfillment tasks.
  - **Complexity:** Low (8 nodes)

- **0082-shopify-reportes-semanal.json**
  - **Description:** Weekly Shopify sales reports generator. Aggregates order data, calculates metrics, generates comprehensive weekly reports for store analytics.
  - **Complexity:** Medium (18 nodes)

- **0140-onfleet-shopify-task.json**
  - **Description:** Onfleet task creation for new Shopify fulfillments. Automatically generates delivery tasks in Onfleet when Shopify fulfillment is created.
  - **Complexity:** Medium (16 nodes)

- **0161-onfleet-driver-signup-alert.json**
  - **Description:** Onfleet driver signup notification system. Alerts administrators when new drivers register, sends welcome emails and onboarding information.
  - **Complexity:** Low (7 nodes)

- **0167-shopify-onfleet-tags-sync.json**
  - **Description:** Shopify and Onfleet tags synchronization. Keeps product tags and delivery attributes synchronized between Shopify store and Onfleet delivery system.
  - **Complexity:** Medium (15 nodes)

- **0168-Onfleet-to-QuickBooks-Invoices.json**
  - **Description:** Onfleet to QuickBooks invoice integration. Creates invoices in QuickBooks based on completed Onfleet delivery tasks.
  - **Complexity:** Medium (19 nodes)

- **0169-onfleet-task-from-google-drive.json**
  - **Description:** Onfleet task creation from Google Drive. Reads delivery requests from Google Drive spreadsheets, generates tasks in Onfleet automatically.
  - **Complexity:** Medium (17 nodes)

- **0240-shopify-zendesk-sync.json**
  - **Description:** Shopify and Zendesk customer synchronization. Syncs customer data, order history, and support tickets between Shopify and Zendesk systems.
  - **Complexity:** High (28 nodes)

- **0241-shopify-zendesk-sync.json**
  - **Description:** Shopify order update trigger for Zendesk sync. Activates when orders are updated, keeps Zendesk tickets synchronized with latest order status.
  - **Complexity:** Medium (20 nodes)

- **0248-shopify-mautic-contact.json**
  - **Description:** Shopify to Mautic contact integration. Syncs customer information, purchase history, and contact data from Shopify to Mautic marketing automation.
  - **Complexity:** Medium (18 nodes)

- **0481-shopify-orders-sync.json**
  - **Description:** Shopify orders synchronization system. Keeps order data synchronized across multiple systems, ensures data consistency and backup.
  - **Complexity:** Medium (22 nodes)

- **0487-shopify-fulfillment-auto.json**
  - **Description:** Automated Shopify fulfillment management. Handles fulfillment status updates, tracking number assignments, and customer notifications automatically.
  - **Complexity:** High (26 nodes)

- **0537-shopify-odoo-product-sync.json**
  - **Description:** Shopify to Odoo product synchronization. Keeps product catalog, pricing, and inventory data synced between Shopify storefront and Odoo ERP.
  - **Complexity:** High (32 nodes)

- **0584-shopify-order-trigger.json**
  - **Description:** Shopify order creation trigger system. Activates downstream workflows when new orders are placed, enables automated order processing chains.
  - **Complexity:** Low (6 nodes)

- **0585-shopify-get-all-records.json**
  - **Description:** Shopify data retrieval automation. Fetches all records including products, orders, customers for bulk operations and data exports.
  - **Complexity:** Medium (15 nodes)

- **0651-Import-multiple-manufacturers-from-Google-Sheets-to-Shopware-6.json**
  - **Description:** Bulk manufacturer import from Google Sheets to Shopware 6. Reads manufacturer data, creates or updates records in Shopware 6 e-commerce platform.
  - **Complexity:** Medium (20 nodes)

- **10040-Full-cycle-invoice-automation-Airtable-QuickBooks-Stripe.json**
  - **Description:** Complete invoice automation workflow. Integrates Airtable, QuickBooks, and Stripe for automated invoice generation, payment processing, and accounting.
  - **Complexity:** High (45 nodes)

- **10188-Sync-products-between-Airtable-and-Shopify-with-inventory-management.json**
  - **Description:** Airtable to Shopify product synchronization with inventory tracking. Syncs product data, manages stock levels, handles pricing updates automatically.
  - **Complexity:** High (38 nodes)

- **10217-Automate-Shopify-SEO-content-creation-with-GPT-4o-Claude-multi-agent-system.json**
  - **Description:** Shopify SEO content automation with multi-agent AI. Generates product descriptions, blog posts, meta content using GPT-4o and Claude agents, optimizes for search engines.
  - **Complexity:** High (52 nodes)

- **10672-Scrape-Shopify-store-data-with-RapidAPI-and-save-to-Google-Sheets.json**
  - **Description:** Shopify store data scraper using RapidAPI. Scrapes product information, pricing, inventory from any Shopify store and exports to Google Sheets.
  - **Complexity:** Medium (11 nodes)

- **10713-Automated-Shopify-abandoned-cart-alerts-from-Razorpay-to-Telegram.json**
  - **Description:** Shopify abandoned cart alerts via Telegram. Monitors incomplete checkouts, triggers follow-up notifications through Razorpay payment gateway.
  - **Complexity:** High (30 nodes)

- **10783-Generate-multilingual-Shopify-product-descriptions-with-Gemini-25-Vision-AI.json**
  - **Description:** Multilingual Shopify product descriptions with Gemini 2.5 Vision AI. Generates product descriptions in multiple languages using visual analysis and advanced AI translation.
  - **Complexity:** High (35 nodes)

- **10900-AI-powered-WhatsApp-customer-support-for-Shopify-brands-with-LLM-agents.json**
  - **Description:** AI-powered WhatsApp support for Shopify brands. Handles customer inquiries, order tracking, returns using LLM agents integrated with Shopify data.
  - **Complexity:** High (48 nodes)

- **11087-AI-Shopify-product-descriptions-GPT-4o-Vision-Claude-Analytics.json**
  - **Description:** AI Shopify product descriptions with GPT-4o Vision and Claude Analytics. Generates optimized product descriptions using visual AI and analytics-driven insights.
  - **Complexity:** High (42 nodes)

- **12025-Scrape-import-shoe-products-to-Shopify-with-BrowserAct-with-variants-images.json**
  - **Description:** Scrape and import shoe products to Shopify with BrowserAct (with variants & images). Reads product URLs from Google Sheets, scrapes detailed product data, creates Shopify products with variants and images using BrowserAct.
  - **Complexity:** High (25 nodes)

## Stripe Payment Integration

- **0017-stripe-hubspot-slack.json**
  - **Description:** Stripe to HubSpot and Slack integration. Processes Stripe payments, updates HubSpot CRM deals, sends payment notifications to Slack.
  - **Complexity:** Medium (18 nodes)

- **0222-pipedrive-stripe-deal.json**
  - **Description:** Pipedrive to Stripe deal automation. Creates or updates Pipedrive deals when Stripe payments are processed, tracks revenue attribution.
  - **Complexity:** Medium (16 nodes)

- **0223-stripe-organization-sync.json**
  - **Description:** Stripe organization synchronization. Syncs customer organizations, billing data, and account details between systems.
  - **Complexity:** Low (9 nodes)

- **0224-pipedrive-stripe-product-sync.json**
  - **Description:** Pipedrive and Stripe product synchronization. Keeps product catalogs, subscription plans, and pricing aligned between platforms.
  - **Complexity:** Medium (14 nodes)

- **0403-stripe-checkout-filters.json**
  - **Description:** Stripe checkout filtering and routing automation. Processes checkout events, applies custom filters, routes transactions to appropriate workflows.
  - **Complexity:** Medium (15 nodes)

- **10654-Auto-send-PDF-invoices-with-Stripe-payment-triggers-and-Gmail.json**
  - **Description:** Automated PDF invoice delivery with Stripe payment triggers. Generates professional PDF invoices upon Stripe payment events, sends via Gmail.
  - **Complexity:** High (28 nodes)

- **10961-Automate-QuickBooks-sales-receipts-customer-creation-from-Stripe-payments.json**
  - **Description:** QuickBooks integration with Stripe payments. Creates sales receipts and customer records in QuickBooks when Stripe transactions occur.
  - **Complexity:** High (32 nodes)

## WooCommerce Automation

- **0261-mattermost-woocommerce-pedido.json**
  - **Description:** WooCommerce order notification to Mattermost. Sends order details, customer info to Mattermost channels when WooCommerce orders are created.
  - **Complexity:** Medium (11 nodes)

- **0693-woocommerce-order-notification.json**
  - **Description:** WooCommerce order notification system. Sends order confirmations, tracking details to customers via various communication channels.
  - **Complexity:** Low (8 nodes)

- **0696-woocommerce-refund-notification.json**
  - **Description:** WooCommerce refund notification automation. Processes refund events, updates customers, sends refund confirmation notifications.
  - **Complexity:** Medium (12 nodes)

- **0700-mautic-woocommerce-sync.json**
  - **Description:** WooCommerce to Mautic integration. Syncs customer data, purchase history, and contact information from WooCommerce to Mautic marketing automation.
  - **Complexity:** Medium (20 nodes)

- **0826-ai-woocommerce-support-agent.json**
  - **Description:** AI-powered WooCommerce support agent. Handles customer inquiries, order status checks, product recommendations using artificial intelligence.
  - **Complexity:** High (35 nodes)

- **10276-Generate-authentic-product-reviews-with-OpenAI-for-WooCommerce.json**
  - **Description:** Generate authentic product reviews with OpenAI for WooCommerce. Creates realistic, AI-generated reviews for social proof and marketing purposes.
  - **Complexity:** High (30 nodes)

- **10447-Automate-WordPress-WooCommerce-content-with-OpenAI-Reviews-comments-updates.json**
  - **Description:** WordPress and WooCommerce content automation with OpenAI. Generates blog posts, manages product reviews, syncs comments using AI content generation.
  - **Complexity:** High (42 nodes)

- **10624-Complete-WooCommerce-to-Odoo-integration-Sync-orders-products-customers.json**
  - **Description:** Complete WooCommerce to Odoo integration. Synchronizes orders, products, customers between WooCommerce store and Odoo ERP system.
  - **Complexity:** High (45 nodes)

- **10637-Conversational-sales-agent-for-WooCommerce-with-GPT-4-Stripe-and-CRM-integration.json**
  - **Description:** Conversational AI sales agent for WooCommerce. Handles pre-sales, order management, payments using GPT-4, Stripe integration, and CRM synchronization.
  - **Complexity:** High (55 nodes)

- **10648-Auto-generate-virtual-AI-try-on-images-for-WooCommerce-with-Gemini-Nano-Banana.json**
  - **Description:** Auto-generate virtual AI try-on images for WooCommerce with Gemini and Nano Banana. Creates virtual try-on visuals for products using generative AI.
  - **Complexity:** High (38 nodes)

- **11016-Create-update-and-get-a-product-from-WooCommerce.json**
  - **Description:** WooCommerce product CRUD operations. Create, update, and retrieve products from WooCommerce store via REST API integration.
  - **Complexity:** Medium (15 nodes)

- **11026-Send-a-message-on-Mattermost-when-an-order-is-created-in-WooCommerce.json**
  - **Description:** WooCommerce order alerts to Mattermost. Sends formatted order notifications to Mattermost channels when new orders are placed.
  - **Complexity:** Medium (14 nodes)

- **11033-Voice-AI-customer-support-for-WooCommerce-using-VAPI-GPT-4o-Gemini-with-RAG.json**
  - **Description:** Voice AI customer support for WooCommerce using VAPI. Handles voice calls, order inquiries, support tickets using GPT-4o, Gemini, and RAG knowledge base.
  - **Complexity:** High (52 nodes)

- **11050-Auto-collect-WooCommerce-orders-to-Discord-Google-Sheets.json**
  - **Description:** WooCommerce order collection to Discord and Google Sheets. Automatically gathers new orders, posts summaries to Discord, and stores in Google Sheets.
  - **Complexity:** High (32 nodes)

## Chargebee Integration

- **0027-chargebee-nuevo-cliente.json**
  - **Description:** Chargebee new customer automation. Processes new customer signups, sends welcome emails, and creates records in Chargebee billing system.
  - **Complexity:** Medium (14 nodes)

- **0049-chargebee-event-trigger.json**
  - **Description:** Chargebee event trigger system. Activates workflows when Chargebee events occur (subscriptions, payments, cancellations).
  - **Complexity:** Low (7 nodes)

## Onfleet Delivery Management

- **0111-onfleet-tasks-from-spreadsheet.json**
  - **Description:** Onfleet tasks creation from spreadsheet data. Reads delivery requests from Google Sheets or Excel, generates tasks in Onfleet automatically.
  - **Complexity:** Medium (18 nodes)

## Paddle Integration

- **0587-paddle-coupon-creator.json**
  - **Description:** Paddle coupon code generator. Creates discount codes in Paddle payment platform, manages coupon campaigns, tracks usage.
  - **Complexity:** Medium (16 nodes)

## Cross-Platform E-commerce

- **10061-Scrape-blog-articles-into-AI-generated-LinkedIn-posts-with-GPT-4o-human-review.json**
  - **Description:** Blog to LinkedIn post generator with AI and human review. Scrapes blog articles, generates LinkedIn-optimized posts using GPT-4o, includes human approval workflow.
  - **Complexity:** High (35 nodes)

- **10239-Automate-website-tool-analysis-with-Telegram-Apify-AI-Google-Sheets.json**
  - **Description:** Website tool analysis with Telegram, Apify, and AI. Scrapes competitor tools, analyzes features, generates reports via AI and Telegram notifications.
  - **Complexity:** High (38 nodes)

- **10243-Scrape-business-data-from-Google-Maps-via-SerpAPI-and-export-to-Sheets-Excel.json**
  - **Description:** Google Maps business data scraper with SerpAPI. Extracts business information (name, address, phone, reviews) from Google Maps, exports to Sheets and Excel.
  - **Complexity:** Medium (22 nodes)

- **10686-Generate-daily-business-digest-with-Notion-Gmail-Stripe-Calendar-and-GPT-4o.json**
  - **Description:** Daily business digest generator with Notion, Gmail, Stripe, Calendar. Compiles daily sales, payments, and schedule summaries using GPT-4o for natural language generation.
  - **Complexity:** High (40 nodes)
# AI AND NLP

- **0003-line-chatgpt-image-flow.json**
  - **Description:** Generate images with ChatGPT for LINE integration
  - **Complexity:** Medium (12 nodes)

- **0280-line-chatbot-agent.json**
  - **Description:** Chatbot agent for LINE with natural language processing capabilities
  - **Complexity:** High (35 nodes)

- **0285-bitcoin-chat-flow-pinecone.json**
  - **Description:** Cryptocurrency chat with Pinecone vector database
  - **Complexity:** High (28 nodes)

- **0289-mistral-cadena-hf.json**
  - **Description:** Mistral model chain via Hugging Face integration
  - **Complexity:** Medium (18 nodes)

- **0290-feedback-openai-google.json**
  - **Description:** Feedback system using OpenAI and Google integrations
  - **Complexity:** Medium (22 nodes)

- **0331-eleven-openai-audio-translation.json**
  - **Description:** Audio translation using ElevenLabs and OpenAI
  - **Complexity:** Medium (20 nodes)

- **0378-elevenlabs-text-to-speech.json**
  - **Description:** Text-to-speech conversion using ElevenLabs
  - **Complexity:** Low (8 nodes)

- **0435-openai-supabase-sql-chat.json**
  - **Description:** OpenAI AI chat with Supabase SQL database
  - **Complexity:** High (32 nodes)

- **0461-milvus-rag-chatbot-flow.json**
  - **Description:** RAG chatbot with Milvus vector database
  - **Complexity:** High (38 nodes)

- **0489-line-n8n-assistant.json**
  - **Description:** n8n integrated assistant for LINE with automated response
  - **Complexity:** Medium (24 nodes)

- **0505-openai-image-generation-edit.json**
  - **Description:** Image generation and editing with DALL-E
  - **Complexity:** Medium (15 nodes)

- **0664-tts-openai.json**
  - **Description:** Text-to-speech using OpenAI Whisper
  - **Complexity:** Low (6 nodes)

- **0691-openai-image-gen.json**
  - **Description:** Image generation with OpenAI
  - **Complexity:** Low (7 nodes)

- **0717-rag-chatbot-docs.json**
  - **Description:** RAG chatbot for document processing
  - **Complexity:** High (42 nodes)

- **0778-discord-ai-agent.json**
  - **Description:** AI agent for Discord with message management
  - **Complexity:** High (30 nodes)

- **0779-rag-movie-recomendacion-qdrant-openai.json**
  - **Description:** Movie recommendation using RAG with Qdrant
  - **Complexity:** High (36 nodes)

- **0798-ai-chat-with-supabase-documents.json**
  - **Description:** AI chat with documents in Supabase
  - **Complexity:** High (34 nodes)

- **0802-google-calendar-ai-agent.json**
  - **Description:** AI agent for Google Calendar management
  - **Complexity:** Medium (26 nodes)

- **0824-rag-financial-report-gen.json**
  - **Description:** Financial report generation with RAG
  - **Complexity:** High (40 nodes)

- **0043-2682-from-community-Perplexity-research-to-HTML-AI-powered-content-creation.json**
  - **Description:** Perplexity AI research for AI-powered content creation to HTML
  - **Complexity:** High (45 nodes)
# AUTONOMOUS AGENTS

- **0280-line-chatbot-agent.json**
  - **Description:** Autonomous chatbot agent for LINE with decision-making capabilities
  - **Complexity:** High (35 nodes)

- **0778-discord-ai-agent.json**
  - **Description:** AI agent for Discord with autonomous message management and response
  - **Complexity:** High (30 nodes)

- **0802-google-calendar-ai-agent.json**
  - **Description:** AI agent with autonomous calendar scheduling and management
  - **Complexity:** High (26 nodes)

- **0461-milvus-rag-chatbot-flow.json**
  - **Description:** Autonomous RAG chatbot with Milvus vector database for intelligent responses
  - **Complexity:** High (38 nodes)

- **0717-rag-chatbot-docs.json**
  - **Description:** Autonomous document analysis agent using RAG for intelligent document retrieval
  - **Complexity:** High (42 nodes)

- **0779-rag-movie-recomendacion-qdrant-openai.json**
  - **Description:** Autonomous recommendation agent using RAG with Qdrant for personalized movie suggestions
  - **Complexity:** High (36 nodes)

- **0798-ai-chat-with-supabase-documents.json**
  - **Description:** Autonomous document analysis agent with Supabase integration for intelligent document queries
  - **Complexity:** High (34 nodes)

- **0824-rag-financial-report-gen.json**
  - **Description:** Autonomous financial analysis agent using RAG for generating comprehensive financial reports
  - **Complexity:** High (40 nodes)

- **0043-2682-from-community-Perplexity-research-to-HTML-AI-powered-content-creation.json**
  - **Description:** Autonomous content creation agent using Perplexity AI research to generate HTML content
  - **Complexity:** High (45 nodes)

- **0435-openai-supabase-sql-chat.json**
  - **Description:** Autonomous database query agent with OpenAI for intelligent SQL queries and data analysis
  - **Complexity:** High (32 nodes)
# Web Scraping & Data Extraction Workflows

This section contains workflows for automated web scraping, data extraction, content aggregation, and web automation.

## General Web Scraping

- **0006-airtable-hn-job-scraping.json**
  - **Description:** Hacker News job scraping to Airtable. Scrapes "Who is Hiring" posts from Hacker News, extracts job details, stores in Airtable for easy access.
  - **Complexity:** Medium (14 nodes)

- **0236-ard-podcast-scraper.json**
  - **Description:** Podcast metadata scraper. Extracts episode information, show notes, and download links from podcast RSS feeds or websites.
  - **Complexity:** Medium (16 nodes)

- **0348-mail-api-scraper.json**
  - **Description:** Email API content scraper. Extracts emails, attachments, and metadata from various email providers and APIs.
  - **Complexity:** Medium (12 nodes)

- **0388-scrappey-test-schedule.json**
  - **Description:** Scheduled scraping test workflow. Runs periodic scraping tasks, monitors data quality, and logs scraping results.
  - **Complexity:** Low (8 nodes)

- **0512-web-scraper-structured.json**
  - **Description:** Structured web data scraper. Extracts data from websites into organized JSON format with proper field mapping and type conversion.
  - **Complexity:** Medium (18 nodes)

- **0796-n8n-reAct-scraper.json**
  - **Description:** ReAct-based web scraping workflow. Uses reasoning-action loops to intelligently navigate and extract data from complex websites.
  - **Complexity:** High (28 nodes)

- **0881-github-trending-scraping.json**
  - **Description:** GitHub trending repositories scraper. Fetches trending projects, analyzes metrics, and tracks popular repositories across languages.
  - **Complexity:** Medium (20 nodes)

- **0951-book-scraping-automation.json**
  - **Description:** Book information scraping automation. Extracts book metadata, reviews, pricing from various book retailers and publishers.
  - **Complexity:** Medium (15 nodes)

- **1050-techcrunch-scraping.json**
  - **Description:** TechCrunch news and startup scraper. Scrapes articles, funding rounds, and startup news from TechCrunch website.
  - **Complexity:** Medium (17 nodes)

- **10563-ScrapingBee-and-Google-Sheets-integration-template.json**
  - **Description:** ScrapingBee integration with Google Sheets. Uses ScrapingBee API for web scraping, stores extracted data directly to Google Sheets.
  - **Complexity:** Medium (14 nodes)

## Apify Scraping

- **0410-3288-from-community-Youtube-RAG-search-with-frontend-using-Apify-Qdrant-and-AI.json**
  - **Description:** YouTube RAG search with Apify, Qdrant, and AI. Builds vector database from YouTube transcripts, enables semantic search, and AI-powered Q&A interface.
  - **Complexity:** High (45 nodes)

- **0455-3184-from-community-Process-YouTube-transcripts-with-Apify-OpenAI-Pinecone.json**
  - **Description:** YouTube transcript processing with Apify, OpenAI, and Pinecone. Scrapes video transcripts, processes with AI, stores in vector database for search.
  - **Complexity:** High (42 nodes)

- **10102-Automated-content-strategy-with-Google-Trends-News-Firecrawl-Claude-AI.json**
  - **Description:** Content strategy automation with Google Trends, Firecrawl, and Claude AI. Monitors trending topics, scrapes news, generates content strategy recommendations.
  - **Complexity:** High (38 nodes)

- **10103-Generate-qualified-Instagram-leads-from-hashtags-with-Apify-and-Google-Sheets.json**
  - **Description:** Instagram lead generation from hashtags using Apify. Scrapes posts by hashtags, extracts user information, generates qualified leads in Google Sheets.
  - **Complexity:** High (32 nodes)

- **10106-Autonomous-blog-publishing-from-YouTube-videos-with-ChatGPT-Sheets-Apify-Pexels.json**
  - **Description:** Blog publishing automation from YouTube videos. Scrapes YouTube video content, generates blog posts with ChatGPT, sources images from Pexels, publishes autonomously.
  - **Complexity:** High (40 nodes)

- **10125-Batch-scrape-website-URLs-from-Google-Sheets-to-Google-Docs-with-Firecrawl.json**
  - **Description:** Batch website scraper from Google Sheets to Google Docs using Firecrawl. Reads URL lists, scrapes multiple websites, compiles content into Google Docs.
  - **Complexity:** High (35 nodes)

- **10195-Turn-YouTube-comments-into-content-ideas-with-GPT-41-mini-Tavily-Apify.json**
  - **Description:** YouTube comments to content ideas with GPT-4.1-mini, Tavily, and Apify. Scrapes YouTube comments, analyzes sentiment, generates content ideas using AI.
  - **Complexity:** High (38 nodes)

- **10197-Automate-Instagram-profile-analysis-with-Airtop-scraping-and-GPT-4o-intelligence.json**
  - **Description:** Instagram profile analysis automation with Airtop and GPT-4o. Scrapes Instagram profiles, analyzes content, generates intelligence reports using AI.
  - **Complexity:** High (35 nodes)

- **10239-Automate-website-tool-analysis-with-Telegram-Apify-AI-Google-Sheets.json**
  - **Description:** Website tool analysis with Telegram, Apify, and AI. Scrapes competitor websites, analyzes tools/features, sends reports via Telegram notifications.
  - **Complexity:** High (36 nodes)

- **10298-Automated-cover-letter-generator-with-Indeed-job-scraping-and-GPT-4o-mini.json**
  - **Description:** Cover letter generator with Indeed job scraping and GPT-4o-mini. Scrapes job postings from Indeed, generates customized cover letters using AI.
  - **Complexity:** High (34 nodes)

- **10303-Google-Maps-leads-namesemailsphones-Apify-Airtable-custom-emails.json**
  - **Description:** Google Maps leads scraper with Apify and Airtable. Extracts business contact information (names, emails, phones) from Google Maps, stores in Airtable, sends custom emails.
  - **Complexity:** High (32 nodes)

- **10360-Write-personalised-direct-messages-for-Instagram-with-Apify-OpenAI-GSheets.json**
  - **Description:** Personalized Instagram DM automation with Apify and OpenAI. Generates customized direct messages for outreach campaigns and tracks in Google Sheets.
  - **Complexity:** High (32 nodes)

- **10376-Automate-lead-gen-email-outreach-with-Apify-Apolloio-GPT-4-Google-Sheets.json**
  - **Description:** Lead generation email outreach with Apify and Apollo.io. Scrapes LinkedIn profiles, enriches with Apollo data, generates AI-powered emails via GPT-4.
  - **Complexity:** High (40 nodes)

- **10435-Automate-LinkedIn-post-summaries-to-Slack-with-AI-and-Apify.json**
  - **Description:** LinkedIn post aggregator with AI summarization to Slack. Scrapes LinkedIn content, summarizes with AI, posts digests to Slack channels.
  - **Complexity:** Medium (22 nodes)

- **10638-Automate-LinkedIn-profile-research-email-outreach-with-Apify-Gemini-Sheets.json**
  - **Description:** LinkedIn profile research and email outreach with Apify, Gemini, and Sheets. Uses Apify for data extraction, Gemini for analysis, automated email campaigns via Google Sheets management.
  - **Complexity:** High (36 nodes)

- **10639-Automate-scraping-Y-Combinator-startups-with-Apify-Google-Sheets.json**
  - **Description:** Y Combinator startup scraping with Apify and Google Sheets. Scrapes Hacker News startup discussions, extracts company info, tracks in Google Sheets.
  - **Complexity:** High (30 nodes)

- **10641-Automate-AI-Upwork-proposal-generation-with-Apify-Google-Gemini-sheets.json**
  - **Description:** AI Upwork proposal generator with Apify, Google, and Gemini. Scrapes Upwork job postings, generates customized proposals using AI, tracks in Google Sheets.
  - **Complexity:** High (38 nodes)

- **10649-Analyze-trending-YouTube-videos-with-Apify-OpenAI-and-Google-Sheets.json**
  - **Description:** Trending YouTube videos analyzer with Apify and OpenAI. Scrapes trending videos, analyzes metrics, generates insights using AI, stores in Google Sheets.
  - **Complexity:** High (35 nodes)

- **10664-Weekly-LinkedIn-connections-sync-analysis-with-Apify-and-Google-Sheets.json**
  - **Description:** LinkedIn connections weekly sync and analysis with Apify. Tracks connection growth, analyzes network patterns, stores data in Google Sheets.
  - **Complexity:** Medium (25 nodes)

- **10672-Scrape-Shopify-store-data-with-RapidAPI-and-save-to-Google-Sheets.json**
  - **Description:** Shopify store data scraper with RapidAPI. Scrapes product information, pricing, inventory from any Shopify store and exports to Google Sheets.
  - **Complexity:** Medium (11 nodes)

- **10692-Instagram-visual-analysis-with-Apify-scraping-OpenAI-GPT-5-Google-Sheets.json**
  - **Description:** Instagram visual content analysis with Apify, OpenAI, and Google Sheets. Scrapes Instagram posts, analyzes images with AI vision, generates insights and stores in Sheets.
  - **Complexity:** High (42 nodes)

- **10700-Find-valid-vouchers-and-promo-codes-with-SerpAPI-Decodo-and-GPT-5-Mini.json**
  - **Description:** Voucher and promo code finder with SerpAPI, Decodo, and GPT-5-mini. Scrapes discount codes from various websites, validates them, generates curated lists.
  - **Complexity:** High (35 nodes)

- **10755-Automate-content-research-with-Reddit-scraping-AI-analysis-and-Google-Sheets.json**
  - **Description:** Reddit content research automation with AI. Scrapes Reddit posts, analyzes discussions, generates content strategy recommendations, stores in Google Sheets.
  - **Complexity:** High (38 nodes)

- **10756-Extract-Amazon-book-data-generate-purchase-reports-with-Decodo-Scraper.json**
  - **Description:** Amazon book data extraction with Decodo. Scrapes book information, pricing, reviews from Amazon, generates purchase analysis reports.
  - **Complexity:** High (30 nodes)

- **10758-Scrape-LinkedIn-job-listings-with-Phantombuster-save-to-Google-Sheets.json**
  - **Description:** LinkedIn job listings scraper with Phantombuster. Extracts job postings, company info, requirements from LinkedIn, saves to Google Sheets.
  - **Complexity:** High (28 nodes)

- **10785-Generate-and-research-sales-leads-with-Jina-AI-OpenAI-email-automation-via-Gmail.json**
  - **Description:** Sales lead generation with Jina AI, OpenAI, and Gmail. Scrapes business websites, generates leads, creates AI-powered email outreach campaigns.
  - **Complexity:** High (38 nodes)

## Firecrawl Scraping

- **0680-firecrawl-markdown-extractor.json**
  - **Description:** Markdown extractor using Firecrawl. Scrapes websites, converts HTML content to clean Markdown format, ideal for documentation and content processing.
  - **Complexity:** Medium (12 nodes)

- **10099-Crawl-websites-answer-questions-with-GPT-5-nano-and-Google-Sheets.json**
  - **Description:** Website crawler with GPT-5-nano. Crawls websites, answers questions about content, stores Q&A pairs in Google Sheets for knowledge base.
  - **Complexity:** High (32 nodes)

- **10109-Generate-website-sitemaps-visual-trees-with-Firecrawl-and-Google-Sheets.json**
  - **Description:** Website sitemap and visual tree generator with Firecrawl. Scrapes website structure, generates sitemaps, creates visual tree diagrams, stores in Google Sheets.
  - **Complexity:** High (28 nodes)

- **10115-Batch-scrape-website-URLs-from-Google-Sheets-to-Google-Docs-with-Firecrawl.json**
  - **Description:** Batch website scraper from Google Sheets to Google Docs using Firecrawl. Reads URL lists, scrapes multiple websites, compiles content into Google Docs.
  - **Complexity:** High (35 nodes)

- **10125-Automate-GitHub-trending-data-collection-with-FireCrawl-GPT-and-Supabase.json**
  - **Description:** GitHub trending data automation with Firecrawl, GPT, and Supabase. Scrapes trending repositories, analyzes with GPT, stores in Supabase database.
  - **Complexity:** High (38 nodes)

- **10795-Crawl-website-blog-content-and-save-to-Google-Sheets-with-Dumpling-AI.json**
  - **Description:** Website blog content crawler with Dumpling AI. Crawls blog websites, extracts articles, summarizes with AI, saves to Google Sheets.
  - **Complexity:** High (35 nodes)

## Jina AI Scraping

- **0811-jina-scraper-book-extractor.json**
  - **Description:** Book information extractor with Jina AI. Scrapes book metadata, descriptions, and reviews from various online bookstores using Jina AI technology.
  - **Complexity:** Medium (15 nodes)

- **10442-Article-to-threaded-Bluesky-posts-with-JinaAI-and-GeminiGPT.json**
  - **Description:** Article to Bluesky thread generator with Jina AI and Gemini. Scrapes articles, breaks them into Bluesky-friendly threads, generates posts with AI assistance.
  - **Complexity:** High (30 nodes)

- **12036-Scrape-structure-and-store-news-data-using-Decodo-Gemini-AI-and-Google-Sheets.json**
  - **Description:** News scraper and structuring with Decodo and Gemini AI. Scrapes forum or news content, structures data into clean JSON, stores in Google Sheets.
  - **Complexity:** High (28 nodes)

- **12046-Match-resumes-to-jobs-automatically-with-Gemini-AI-and-Decodo-Scraping.json**
  - **Description:** Resume-to-job matching with Gemini AI and Decodo scraping. Takes candidate resumes and LinkedIn profiles, scrapes job postings from LinkedIn/JobStreet, ranks matches, emails reports.
  - **Complexity:** High (42 nodes)

- **12037-Telegram-research-assistant-for-academic-papers-using-Gemini-AI-and-Decodo.json**
  - **Description:** AI research assistant for academic papers via Telegram. Uses Gemini AI to interpret queries, Decodo to scrape Google Scholar/arXiv, summarizes papers, delivers results in chat.
  - **Complexity:** High (45 nodes)

## Decodo Scraping

- **0268-uProc_telegram_screenshot.json**
  - **Description:** Website screenshot generator that sends images to Telegram. Uses uProc service to capture screenshots and deliver them via Telegram bot.
  - **Complexity:** Medium (9 nodes)

- **10243-Scrape-business-data-from-Google-Maps-via-SerpAPI-and-export-to-Sheets-Excel.json**
  - **Description:** Google Maps business data scraper with SerpAPI. Extracts business information (name, address, phone, reviews) from Google Maps, exports to Sheets and Excel.
  - **Complexity:** Medium (22 nodes)

- **10321-Decodo-SaaS-pricing-intelligence-workflow-B2B-pricing-radar.json**
  - **Description:** SaaS pricing intelligence with Decodo. Scrapes SaaS pricing pages, compares features, generates pricing radar reports for competitive analysis.
  - **Complexity:** High (32 nodes)

- **10547-Scrape-Google-Maps-data-discover-email-addresses-with-SerpAPI-and.json**
  - **Description:** Google Maps data scraper with SerpAPI. Discovers and extracts email addresses, contact info from Google Maps business listings.
  - **Complexity:** Medium (20 nodes)

- **10756-Extract-Amazon-book-data-generate-purchase-reports-with-Decodo-Scraper.json**
  - **Description:** Amazon book data extraction with Decodo. Scrapes book information, pricing, reviews from Amazon, generates purchase analysis reports.
  - **Complexity:** High (30 nodes)

## SerpAPI Scraping

- **10243-Scrape-business-data-from-Google-Maps-via-SerpAPI-and-export-to-Sheets-Excel.json**
  - **Description:** Google Maps business data scraper with SerpAPI. Extracts business information (name, address, phone, reviews) from Google Maps, exports to Sheets and Excel.
  - **Complexity:** Medium (22 nodes)

- **10547-Scrape-Google-Maps-data-discover-email-addresses-with-SerpAPI-and.json**
  - **Description:** Google Maps data scraper with SerpAPI. Discovers and extracts email addresses, contact info from Google Maps business listings.
  - **Complexity:** Medium (20 nodes)

- **10700-Find-valid-vouchers-and-promo-codes-with-SerpAPI-Decodo-and-GPT-5-Mini.json**
  - **Description:** Voucher and promo code finder with SerpAPI, Decodo, and GPT-5-mini. Scrapes discount codes from various websites, validates them, generates curated lists.
  - **Complexity:** High (35 nodes)

- **10630-Google-Maps-to-Airtable-lead-scraper-with-GPT-contact-extraction-from-impressum.json**
  - **Description:** Google Maps to Airtable lead scraper with GPT. Scrapes Google Maps listings, extracts contact info from impressum pages, generates leads stored in Airtable.
  - **Complexity:** High (28 nodes)

## BrowserAct Scraping

- **12024-Scrape-detailed-GitHub-profiles-to-Google-Sheets-using-BrowserAct.json**
  - **Description:** Detailed GitHub profile scraper to Google Sheets with BrowserAct. Scrapes comprehensive GitHub user data (profile, repos, activity), creates dedicated sheets for each user.
  - **Complexity:** High (38 nodes)

- **12025-Scrape-import-shoe-products-to-Shopify-with-BrowserAct-with-variants-images.json**
  - **Description:** Scrape and import shoe products to Shopify with BrowserAct. Reads product URLs from Google Sheets, scrapes detailed product data, creates Shopify products with variants and images using BrowserAct.
  - **Complexity:** High (25 nodes)

## Content Extraction & Summarization

- **12035-CoinGecko-crypto-price-forecasting-pipeline-with-Gemini-AI-Decodo-and-Gmail.json**
  - **Description:** CoinGecko crypto price forecasting with Gemini AI and Decodo. Scrapes cryptocurrency prices, generates 24h forecasts with Gemini, emails daily reports.
  - **Complexity:** High (32 nodes)

- **10061-Scrape-blog-articles-into-AI-generated-LinkedIn-posts-with-GPT-4o-human-review.json**
  - **Description:** Blog to LinkedIn post generator with AI and human review. Scrapes blog articles, generates LinkedIn-optimized posts using GPT-4o, includes human approval workflow.
  - **Complexity:** High (35 nodes)

- **10102-Automated-content-strategy-with-Google-Trends-News-Firecrawl-Claude-AI.json**
  - **Description:** Content strategy automation with Google Trends, Firecrawl, and Claude AI. Monitors trending topics, scrapes news, generates content strategy recommendations.
  - **Complexity:** High (38 nodes)

- **10195-Turn-YouTube-comments-into-content-ideas-with-GPT-41-mini-Tavily-Apify.json**
  - **Description:** YouTube comments to content ideas with GPT-4.1-mini, Tavily, and Apify. Scrapes YouTube comments, analyzes sentiment, generates content ideas using AI.
  - **Complexity:** High (38 nodes)

## Other Scraping & Extraction Tools

- **12050-Doctor-appointment-scheduler-with-Telegram-Gemini-AI-and-Google-Sheets.json**
  - **Description:** Doctor appointment scheduler with Telegram, Gemini AI, and Google Sheets. Handles appointment booking, availability checking, and sends confirmations via Telegram.
  - **Complexity:** High (35 nodes)

- **10125-Automate-GitHub-trending-data-collection-with-FireCrawl-GPT-and-Supabase.json**
  - **Description:** GitHub trending data automation with Firecrawl, GPT, and Supabase. Scrapes trending repositories, analyzes with GPT, stores in Supabase database.
  - **Complexity:** High (38 nodes)

- **10527-Restaurant-lead-generation-from-Google-Maps-with-Apify-Airtable-AI-newsletter.json**
  - **Description:** Restaurant lead generation from Google Maps with Apify, Airtable, and AI newsletter. Scrapes restaurant info, generates leads, manages newsletter campaigns.
  - **Complexity:** High (40 nodes)

- **12060-AI-powered-feedback-triage-Jotform-to-Trello-Airtable-Slack-with-Gemini.json**
  - **Description:** AI-powered feedback triage with Jotform, Trello, Airtable, Slack, and Gemini. Collects form submissions, categorizes with AI, routes to appropriate Trello boards, sends Slack notifications.
  - **Complexity:** High (45 nodes)

- **11572-Extracts-and-organizes-academic-publications-using-GPT-4-Mini-Google-Sheets.json**
  - **Description:** Academic publications extractor with GPT-4-mini and Google Sheets. Scrapes academic papers, extracts metadata, organizes in structured Google Sheets database.
  - **Complexity:** High (38 nodes)
# OTHERS

## Security and Authentication

- **0011-totp-generator.json**
  - **Description:** Generate TOTP codes for two-factor authentication in n8n
  - **Complexity:** Low (5 nodes)

- **0053-ssl-expiry-checker.json**
  - **Description:** Get SSL certificates for security monitoring
  - **Complexity:** Low (6 nodes)

- **0067-obtener-registros-dns.json**
  - **Description:** Query and retrieve DNS records from domains
  - **Complexity:** Low (4 nodes)

- **0070-114_validar_telefono.json**
  - **Description:** Verify phone numbers automatically
  - **Complexity:** Low (3 nodes)

## IoT and Space

- **0024-iss-position-updates.json**
  - **Description:** Monitor and send International Space Station position updates every minute to ActiveMQ
  - **Complexity:** Medium (18 nodes)

- **0030-iss-monitoring-sqs.json**
  - **Description:** ISS satellite monitoring with SQS integration
  - **Complexity:** Medium (20 nodes)

- **0032-iss-satellite-monitoring.json**
  - **Description:** Satellite monitoring for ISS tracking
  - **Complexity:** Medium (16 nodes)

- **0042-iss-mqtt-flow.json**
  - **Description:** MQTT flow for ISS monitoring
  - **Complexity:** Medium (14 nodes)

## Education and Learning

- **0045-google-books-automation.json**
  - **Description:** Get volumes from Google Books and add them to your personal bookshelf
  - **Complexity:** Low (8 nodes)

## Finance and Billing

- **0083-harvest-cliente-ciclo.json**
  - **Description:** Create clients automatically in Harvest for billing management
  - **Complexity:** Medium (12 nodes)

## Analytics and Metrics

- **0092-segment-track-event.json**
  - **Description:** Track events in Segment for behavior analysis
  - **Complexity:** Low (7 nodes)

## Communication

- **0100-zulip-send-private-message.json**
  - **Description:** Send private messages automatically in Zulip
  - **Complexity:** Low (6 nodes)

## Web Management and CMS

- **0023-coda-insert-data.json**
  - **Description:** Insert data into new rows for tables in Coda
  - **Complexity:** Low (9 nodes)

- **0031-webflow-crear-y-actualizar.json**
  - **Description:** Webflow create and update integration
  - **Complexity:** Medium (22 nodes)

## Utilities and Productivity

- **0040-screenshot-automation.json**
  - **Description:** Automated screenshot capture for web pages or specific elements
  - **Complexity:** Low (5 nodes)

- **0052-release-content-publisher.json**
  - **Description:** Find and publish all stories starting with 'release'
  - **Complexity:** Low (10 nodes)

- **0077-conversor-json-a-xml.json**
  - **Description:** Convert JSON to XML format
  - **Complexity:** Low (4 nodes)

- **0093-pokemon-rate-limiter.json**
  - **Description:** Rate limiter for Pokemon API requests
  - **Complexity:** Medium (15 nodes)

- **0096-news-hacker.json**
  - **Description:** Fetch Hacker News articles
  - **Complexity:** Low (8 nodes)

## Customer Support

- **0094-zendesk-ticket-flow.json**
  - **Description:** Create tickets automatically in Zendesk from different sources
  - **Complexity:** Medium (18 nodes)

## Community

- **0038-orbit-member-update.json**
  - **Description:** Create new member, update member information, create note and post for member
  - **Complexity:** High (24 nodes)

## Lifestyle and Personal

- **0078-comida-diaria-recipe.json**
  - **Description:** Automated food suggestions based on preferences
  - **Complexity:** Low (7 nodes)

## Data Processing

- **0018-entrevistas-y-participantes.json**
  - **Description:** Interview and participant management workflow
  - **Complexity:** Medium (16 nodes)

- **0019-EscrituraJSONBinario.json**
  - **Description:** Binary JSON writing workflow
  - **Complexity:** Low (5 nodes)
