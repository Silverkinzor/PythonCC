# Table 11-1: Assert Methods Available from the unittest Module
# Method                Use
# assertEqual(a, b) Verify that a == b
# assertNotEqual(a, b) Verify that a != b
# assertTrue(x) Verify that x is True
# assertFalse(x) Verify that x is False
# assertIn(item, list) Verify that item is in list
# assertNotIn(item, list) Verify that item is not in list

# The thing but with tally functionality

class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
        self.total_responses = {}

    def show_question(self):
        """Show the survey question."""
        print(question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)

    def tally_responses(self):
        """Talley up the responses and store it in a dictionary."""
        tempResponses = self.responses[:]
        for response in set(self.responses[:]):
            self.total_responses[response] = 0              # Defines the entry in the dictionary
            while response in tempResponses:
                tempResponses.remove(response)
                self.total_responses[response] += 1

    def show_total_results(self):
        """Show the tally of all the results that have been given."""
        print('Total survey results:')
        for language, number in self.total_responses.items():
            print(language + ': ' + str(number))

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.store_response('English')
my_survey.store_response('English')
my_survey.store_response('English')
my_survey.store_response('Swahili')

my_survey.show_results()

my_survey.tally_responses()
my_survey.show_total_results()