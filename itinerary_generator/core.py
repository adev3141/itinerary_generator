import logging
import os
import cohere

class CohereModel:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('COHERE_API_KEY')
        if not self.api_key:
            raise ValueError("API key not found. Please set the COHERE_API_KEY environment variable.")
        self.client = cohere.Client(self.api_key)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("CohereModel initialized.")

    def create_prompt(self, responses):
        logging.debug(f"Creating prompt with responses: {responses}")
        prompt = (
            f"You are an experienced travel agent specializing in creating detailed itineraries for trips globally. Your task is to create a realistic and well-organized itinerary, considering travel times, distances, flights, hotels, hostels, camping, airbnbs, couchsurfing options, terrain, local events, and national holidays. Use the following details to craft the itinerary:\n"
            f"- Locations: {responses['locations']}\n"
            f"- Starting Date: {responses['start_date']}\n"
            f"- Number of Nights: {responses['nights']}\n"
            f"- Accommodation Type: {responses['accommodations']}\n"
            f"- Trip Type (Adventure or Laid-back): {responses['type']}\n"
            f"- Group Size: {responses['group_size']}\n\n"
            "Provide a comprehensive plan that includes:\n"
            "- Daily activities and sightseeing spots\n"
            "- Accommodation details for each night\n"
            "- Events or festivals happening during the trip dates and their impact on travel plans\n"
            "- Transportation details between locations, including travel times\n"
            "- Recommendations for local cuisine and dining options"
        )
        logging.debug(f"Prompt created: {prompt}")
        return prompt

    def generate_itinerary(self, prompt):
        logging.debug(f"Generating itinerary with prompt: {prompt}")
        try:
            response = self.client.chat(
                message=prompt,
                model='command-r-plus'
            )
            generated_text = response.text
            logging.info("Itinerary generated successfully.")
            logging.debug(f"Model response: {generated_text}")

            # Check if the generated text is the same as the prompt and use a fallback if necessary
            if generated_text.strip() == prompt.strip():
                generated_text = (
                    "Oooops! Looks like we've reached our daily limit of giving out free itineraries."
                )
            return generated_text
        except Exception as e:
            logging.error(f"Error generating itinerary: {e}")
            raise

def travel(nights, trip_type, group_size, locations, accommodations, start_date):
    cohere_model = CohereModel()
    responses = {
        "locations": locations,
        "start_date": start_date,
        "nights": nights,
        "accommodations": accommodations,
        "type": trip_type,
        "group_size": group_size
    }
    prompt = cohere_model.create_prompt(responses)
    return cohere_model.generate_itinerary(prompt)
