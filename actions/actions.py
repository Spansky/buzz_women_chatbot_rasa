# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

import pandas as pd
import numpy as np
df = pd.read_csv("Corpus.csv")
#
#
class ActionShowIdeas(Action):

    def name(self) -> Text:
        return "action_show_ideas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ideas = df.loc[:,'Idea'].to_list()
        
        ideas = ' ,'.join(ideas)

        print(ideas)
        dispatcher.utter_message(text="You can think about {ideas}".format(ideas = ideas))

        return []


class ActionTakeIdeaForward(Action):

    def name(self) -> Text:
        return "action_take_idea_forward"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Taking your Idea forward")
        dispatcher.utter_message(text="....show corpus data.... of " + tracker.get_slot('idea'))

        return []
