import logging
import os
import cohere

class ItineraryGenerator:
    def __init__(self):
        self.api_key = os.getenv('COHERE_API_KEY')
        if not self.api_key:
            raise ValueError("API key not found. Please set the COHERE_API_KEY environment variable.")
        self.client = cohere.Client(self.api_key)
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("ItineraryGenerator initialized.")

    def generate_itinerary(self, locations, start_date, nights, accommodations, trip_type, group_size):
        prompt = self.create_prompt({
            'locations': locations,
            'start_date': start_date,
            'nights': nights,
            'accommodations': accommodations,
            'type': trip_type,
            'group_size': group_size
        })
        logging.debug(f"Generating itinerary with prompt: {prompt}")
        try:
            response = self.client.chat(
                message=prompt,
                model='command-r-plus'
            )
            generated_text = response.text
            logging.info("Itinerary generated successfully.")
            logging.debug(f"Model response: {generated_text}")
            if generated_text.strip() == prompt.strip():
                generated_text = "Oops! It seems we have encountered an issue. Please try again later."
            return generated_text
        except Exception as e:
            logging.error(f"Error generating itinerary: {e}")
            raise

    def create_prompt(self, responses):
        logging.debug(f"Creating prompt with responses: {responses}")
        return (
            f"You are an experienced travel agent specializing in creating detailed itineraries for trips in Pakistan. "
            f"Your task is to create a realistic and well-organized itinerary, considering travel times, local events, "
            f"and national holidays. Use the following details to craft the itinerary:\n"
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
