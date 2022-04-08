const API_URL='/youtubeVideoSentiment';

window.addEventListener('load', ()=>{
  const button=document.getElementById('submitButton');
  button.addEventListener("click", onSubmit);
});

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

async function onSubmit() {
  const URL=document.getElementById("URL").value;

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


