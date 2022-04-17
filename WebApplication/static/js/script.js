/**
 * This script defines the behaviors for the youtube comment sentiment analysis webapp
 * The script takes a URL for a youtube video from the HTML text input box
 * Calls the youtube sentiment predictor flask api endpoint
 * and returns/prints the percentage of positive comments on the HTML page
 */

//URL for the API that retirieves the ratio of positive to negative comments based on the posted URL
const API_URL='/youtubeVideoSentiment';

//Add an event listener to call our onSubmit function when the submit button is pressed
window.addEventListener('load', ()=>{
  const button=document.getElementById('submitButton');
  button.addEventListener("click", onSubmit);
});

/**
 * Function to get a color and a sentence that summarize the overall sentament based on the sentament ratio
 * @param sentimentRatio (int) the percentage of comments that are predicted to be positive
 * @returns List [color(string), statement(string)] where the color is either red, yellow or green and the statement summarizes the overall sentiment of the comments
 */
function getReccomendation(sentimentRatio){
  var color='';
  var statement='';

  if (45>sentimentRatio && sentimentRatio>0){
    color='red';
    statement='The average sentiment of the comments is negative';
  }
  if (55>sentimentRatio && sentimentRatio>45){
    color='yellow';
    statement='The average sentiment of the comments is neutral';
  }
  if (100>sentimentRatio && sentimentRatio>55){
    color='green';
    statement='The average sentiment of the comments is positive';
  }

  return [color, statement]

}

/**
 * Function to:
 * 1. Get the URL from the HTML text box
 * 2. Call the youtube video comment sentiment analysis with a post request containing the URL
 * 3. Retrieve the sentiment ratio from the response and print the respnse on the HTML page
 */
async function onSubmit() {
  //Get the URL from teh HTML page
  const URL=document.getElementById("URL").value;
  //add the URL to a formatted JSON for our post request
  const URLstring=JSON.stringify({'URL':URL});
  
  const response=await fetch(API_URL, {
    method:"POST",
    body: URLstring,
    headers: {
      "Content-type": "application/json"
    }
      })
      const responseData=await response.json();
      var sentimentRatio=responseData['sentimentRatio'];

      sentimentRatio=Math.round(sentimentRatio*100);
      [color, statement]=getReccomendation(sentimentRatio);

      document.getElementById("sentimentRatio").innerHTML = String(sentimentRatio);
      document.getElementById("sentimentRatio").style.color = color;
      document.getElementById("sentimentDescription").innerHTML = "% of the comments on this video are positive";
      document.getElementById("decision").innerHTML = statement;
      document.getElementById("decision").style.color = color;
}


