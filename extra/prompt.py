# flake8: noqa E501
"""Prompts for using the report builder with the Customer Marketing (CRM) data source"""
from datetime import datetime
from datetime import timezone

# mapping from dimension name to description
# taken from https://knowledgebase.zetaglobal.com/zmp/metrics-and-dimensions-dictionary
_dimensions = {
    "campaign_id": "Campaign identifier code.",
    "account_name": "Displays the name of the account",
    "campaign_name": "Name of Campaign",
    # "occurrence_index": "Index of the Campaign’s Occurrence",
    # "occurrence_sent_at": "Date that the Campaign Occurrence was sent",
    "channel_name": "Defines the channel of execution. Possible values include: Email, SMS, Push, In App, Webhook and Web",
    "converted_site": "The site identifier code where the conversion occurred",
    "message_template_name": "Name of creative sent with the message",
    "device_name": "Name of device a message was first opened on",
    "device_os": "Operating system of device a message was first opened on - MacOS, iOS, Windows, Android etc.",
    "device_type": "The type of device a message was first opened on. Possible values include: Mobile, Desktop, Tablet, Undefined",
    "new_user": "Whether the user was new (first message) when the message was sent. ",
    "preheader_text": "The preheader text associated to a campaign, version, or A/B Variant. ",
    "is_prime_time": "Indicates whether event happened during the defined prime time setting or not. Possible Values include: Yes, No",
    "recipient_domain": "Email domain of the recipient",
    "rec_type": "Type of recommendation included in the message. Possible Values Include: Popular, Personalized",
    "engagement_date": "Date that the message was sent",
    "engagement_month": "Month that the message was sent",
    "engagement_quarter": "Quarter that the message was sent",
    "engagement_week": "Week that the message was sent",
    "engagement_year": "Year that the message was sent",
    "sender_address": "Email address of the sender",
    "sender_domain": "Email domain of the sender",
    "site_id": "Displays the identification code for the site",
    "subject": "The subject line associated to a campaign, version, or A/B Variant",
    "targeted_segment_id": "Targeted Segment identifier code",
    "targeted_segment_name": "Name of segment that was explicitly targeted",
    "template_subject": "The template’s subject line associated to a campaign, version, or A|B variant",
    "variant_name": "Name of A/B test message template",
}
_dimensions_str = "\n".join([f"\t -{dim}: {desc}" for dim, desc in _dimensions.items()])

# mapping from metric name to description
# taken from https://knowledgebase.zetaglobal.com/zmp/metrics-and-dimensions-dictionary
_metrics = {
    "clicks": "The number of unique users who clicked on a linked image or text regardless of the number of times users clicked",
    "average_click_rate": "The average rate at which a message was clicked. Computed as total clicks divided by total clicked messages",
    "average_clicks": "The average number of times individuals clicked a message",
    "average_open_rate": "The average rate at which a message was opened. Computed as total opens divided by total opened messages",
    "average_opens": "The average number of times individuals opened a message",
    "blocked": "The total number of messages for which the message was blocked by the receiving ISP",
    "blocked_rate": "The rate at which messages were blocked by the receiving ISP. Computed as blocks divided by sent",
    "bounce_rate": "The rate at which ZMP received a response from the receiving ISP stating that the message was undeliverable. Computed as bounces (hard + soft) divided by sent",
    "bounces": "The total number of messages for which ZMP received a response from the receiving ISP stating that the message was undeliverable",
    "click_rate": "The rate at which unique users clicked on a linked image or text. Computed as unique messages clicked divided by delivered",
    "complained": "The total number of spam complaints received",
    "complained_rate": "The rate at which spam complaints were received. Computed as complaints divided by delivered",
    "conversions": "For accounts with a site integration and conversion tracking configured, the unique number of users who's conversions were attributed to a particular campaign, regardless of the number of times they converted",
    "ctor": "Stands for Click-To-Open Rate and measures the ratio of individuals that clicked to those individuals that opened",
    "delivered": "The total number of emails successfully delivered to the receiving Inbox Provider. This is only a successful delivery and is not an indication of successful placement in the inbox folder rather than a promotions folder, spam folder or another folder",
    "delivered_rate": "The rate at which messages were successfully delivered to the receiving Inbox Provider. Computed as total delivered divided by total sent",
    "error": "The number of errored events",
    "estimated_open_rate": "Open rate including the server opens by iOS",
    "estimated_opens": "Number of opens estimated using open rate and server opens by iOS",
    "hard_bounced": "The total number of messages for which ZMP received a response from the receiving ISP stating that the message was undeliverable for a permanent reason which cannot/will not be resolved by the inbox owner",
    "hard_bounced_rate": "The rate at which ZMP received a response from the receiving ISP stating that the message was undeliverable for a permanent reason which cannot/will not be resolved by the inbox owner. Computed as hard bounces divided by sent",
    "open_rate": "The rate at which messages were opened. Computed as unique messages opened divided by delivered",
    "opens": "The number of unique messages opened.",
    "other_failure": "The number of times a message failed to send from a campaign for reasons other than bounces.",
    "other_failure_rate": "The rate at which a message failed to send from a campaign for reasons other than bounces. Computed as “other failure” type messages divided by sent",
    "personalization_rate": "The rate that personalized messages were sent. Proportion of messages that had personalized recommendations. Computed as messages with personalized recommendations over total sent",
    "personalized": "Total messages that had personalized recommendations",
    "popular_rate": "The rate at which popular messages were sent. Proportion of messages that had popular recommendations. Computed as messages with popular recommendations over total sent",
    "popular": "Total messages that had popular recommendations",
    "revenue": "For accounts with a site integration, conversion tracking, and revenue tracking configured, the total revenue attributed to a particular campaign",
    "sent": "The total number of emails ZMP attempted to deploy after all exclusions and suppressions",
    "server_opens": "Number of server opens by iOS",
    "soft_bounced": "The total number of messages for which ZMP received a response from the receiving ISP stating that the message was undeliverable for a temporary reason which could be resolved by the inbox owner",
    "soft_bounced_rate": "The rate at which ZMP received a response from the receiving ISP stating that the message was undeliverable for a temporary reason which could be resolved by the inbox owner. Computed as soft bounces divided by sent",
    "throttled": "Number of throttled events",
    "total_click_rate": "The rate at which users clicked on linked images/text in a given message, regardless of the number of times individual users clicked. Computed as total click events divided by delivered",
    "total_clicks": "The total number of times users clicked on linked images/text in a given message",
    "total_conversions": "For accounts with a site integration and conversion tracking, the total number of conversions attributed to a particular campaign",
    "total_ctor": "Stands for Click-To-Open Rate and measures the ratio of total clicks to total opens",
    "total_failure": "The total number of times a message failed to send from a campaign",
    "total_failure_rate": "The rate at which a message failed to send from a campaign. The sum of bounces + blocks + other failures",
    "total_open_rate": "The rate at which messages were opened recorded by ZMP. Relies on an image pixel loading. If a user has images disabled, an open cannot be recorded. Computed as total open events divided by delivered",
    "total_opens": "The total number of opens recorded by ZMP. Relies on an image pixel loading. If a user has images disabled, an open cannot be recorded",
    "true_open_rate": "Open rate calculated excluding the server opens by iOS",
    "true_opens": "Number of opens excluding the server opens by iOS",
    "unsubscribe_rate": "The rate at which individuals unsubscribed to messages. Computed as total unsubscribed messages divided by delivered",
    "unsubscribes": "The total number of individuals who unsubscribed attributed to a particular campaign",
}
_metrics_str = "\n".join([f"\t -{metric}: {desc}" for metric, desc in _metrics.items()])

current_time_utc = datetime.now().astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
# prompt asking LLM to determine which dimensions and metrics to use
PROMPT = f"""Help me augment a set of inputs and outputs for finetuning an llm.
You need to return a json blob with the following instructions.

Try and aggregate across all campaigns, unless otherwise specified.
Also please do not use more than one or two dimensions when using the tool.
When using datetime dimensions such as 'engagement_' try to use the broadest dimension possible,
such as 'engagement_month' instead of 'engagement_date', if it makes sense.

The following dimensions are available.  The name of the dimension is listed first, following by a ":" character,
followed by a description of the dimension.

DIMENSIONS:
{_dimensions_str}

The following metrics are available.  The name of the metric is listed first, following by a ":" character,
followed by a description of the metric.

METRICS:
{_metrics_str}

You will need to determine whether to sort from lowest-to-highest
("ascending") or from highest-to-lowest ("descending").  Use "ascending" sort direction if the user is asking for the
lowest value of the metrics.  Use "descending" for all other cases. For example if the user is asking for the highest
count of a metric like "most clicks", "highest conversions", "best open rate", "best performance", etc. then you should
use "descending" sort direction. If the user asks something like "what is my worst performing campaign/segment?" or
"which of my campaigns has the fewest clicks" or "which subject line results in the lowest open rates", then you should
use "ascending" sort direction.

```json
{{{{
    "dimensions": string \\ comma-separated list of dimensions to use. Each dimension must be one of the available dimensions from earlier.
    "metrics": string \\ comma-separated list of metric to use. Each metric must be one of the available metrics from earlier.
    "sort_direction": string \\ the direction to sort.  Must be either "ascending" or "descending"
}}}}
```

Here are a few examples:

"""
