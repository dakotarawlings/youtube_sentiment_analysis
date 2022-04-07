const API_URL='/youtubeVideoSentiment';

window.addEventListener('load', ()=>{
  const button=document.getElementById('submitButton');
  button.addEventListener("click", onSubmit);
});

function getReccomendation(sentimentRatio){
  const color=''
  const statement=''

  if (45>sentimentRatio>0){
    color='red'
    statement='The overall sentiment in the comments is negative'
  }
  if (55>sentimentRatio>45){
    color='yellow'
    statement='The overall sentiment in the comments is neutral'
  }
  if (100>sentimentRatio>55){
    color='green'
    statement='The overall sentiment in the comments is positive'
  }


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
      const responseData=await response.json()
      const sentimentRatio=responseData['sentimentRatio']

      document.getElementById("sentimentRatio").innerHTML = String(sentimentRatio*100);
      document.getElementById("sentimentRatio").style.color = "#ff0000";

      document.getElementById("sentimentDescription").innerHTML = "% of the comments on this video are positive";
}


