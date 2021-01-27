function updateCounter(){
    fetch('https://fl9uqrmmub.execute-api.us-east-1.amazonaws.com/live',{
        method: 'GET'
    })
  .then(response => {
    if (
        // check if response's status is 200
        response.ok 
    ) {
      return response.json()
    } else {
      throw new Error('something went wrong');
    }
  })
  .then(data => document.getElementById("VisitorCount").innerText = data.Visit_Count)
  console.log("Hello World"); 
  
}
