let Qresponses = ["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree"];

let userQ1 = d3.select("#q1Data");

Qresponses.forEach((response)=>{
    userQ1.append("option")
    .text(response)
    .property("value", response)
});