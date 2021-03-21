function getPercentages(graphSet){
	const percentages = [];
	
	for(let i = 0; i < graphSet.length; i++) {
		const percentage = graphSet[i].getAttribute("data-percent");
		percentages.push(parseFloat(percentage));
	}
	return percentages;
}

function getVoteCount(graphSet){
	const votes = [];
	for(let i = 0; i < graphSet.length; i++) {
    const vote = graphSet[i].getAttribute("data-count");
		votes.push(parseInt(vote));
	}
	return votes;
}

function insertNumbers(graphSet, arr, votesArr){
	arr.forEach((percentage, i) => {
		const graphBar = graphSet[i].querySelector('.graph-bar-'+(i+1)+' .graph-bar-progress');
    const graphBarHTML = document.createElement('span');
		const start_val = 0,
					end_val = [percentage],
					duration = 2000,
					size = 30;
		const svgNumber = d3.select('.graph-number-'+(i+1))
												.append("svg")
												.attr("width", 55)
												.attr("height", size);

    console.log(graphBar);
    const voteCount = votesArr[i];
		svgNumber
      .data(end_val)
      .append("text")
      .text(start_val)
      .attr("class", "txt")
      .attr("y", 23)
      .attr("x", 55)
      .attr("text-anchor", "end")
      .transition()
      .on("start", () => {
        graphBar.append(graphBarHTML);
      })
      .duration(1600)
      .tween("text", function(d) {
          var i = d3.interpolate(this.textContent, d),
              prec = (d + "").split("."),
              round = (prec.length > 1) ? Math.pow(10, prec[1].length) : 1;
          return function(t) {
              const percent = Math.round(i(t) * round) / round;
              // console.log(votesArr[i]);
              this.textContent = voteCount;
              graphBarHTML.style.width = percent+'%';
          };
      });
	});
};

function animateNumbers(list){
	const graphSet = document.querySelector(list).querySelectorAll('li');
  const percentageArr = getPercentages(graphSet);
  const votesArr = getVoteCount(graphSet);

	insertNumbers(graphSet, percentageArr, votesArr);
}

(function initGraph(){
	animateNumbers('.graph-cont');
})();




$("#menu-toggle").click(function(e) {
  e.preventDefault();
  $(".wrapper").toggleClass("toggled"); 
});