import sys, os
import time
import re
from slackclient import SlackClient
from tweet import Tweet

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
UNITED_COMMAND = "united"
MENTION_REGEX = "^<@(UBKLEDGNP)>(.*)"
IRIS = "UBK8WP6UW"

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """

    for event in slack_events:
        print(event)
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel, users):
    """
        Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "Not sure what you mean. Try *{}*.".format(UNITED_COMMAND)

    # Finds and executes the given command, filling in response
    response = None

    # Tweet United
    if command.startswith(UNITED_COMMAND):
        #response = "Sure...write some more code then I can do that!"
        message = command.partition(" ")
        print(command.partition(" "))
        #Tweet.post_message("@someone", message[2])





    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )

    #slack_client.api_call(
    #  "chat.postMessage",
    #  channel=channel,
    #  text="Hello from the bot! :tada:",
    #  user=IRIS
    #)

    slack_client.api_call(
      "conversations.open",
      users=[IRIS]
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        users = slack_client.api_call("users.list")
        for user in users['members']:
            #print(user['display_name_normalized'])
            print(user)  # contains user_id
            print('')
            print(user['profile']) # contains username as display_name_normalized
            print('')
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel, users)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
