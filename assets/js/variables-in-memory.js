document.addEventListener("DOMContentLoaded", function () {
  const svg = d3.select('#variables-in-memory-animation').append('svg')
  .attr('viewBox', `0 0 700 510`)
  .attr('preserveAspectRatio', 'xMidYMid meet')
  .classed('responsive-svg', true);


  const x = 450;
  const y = 40;
  const width = 100;
  const height = 460;
  const segments = 25;
  const segmentHeight = height / segments;
  const offset = 20;
  const text_x = 20;
  const text_h = 30;
  const delayStep = 2000;

  // Static components
  // Draw main rectangle
  svg.append('rect')
    .attr('x', x)
    .attr('y', y)
    .attr('width', width)
    .attr('height', height)
    .attr('fill', 'lightgreen')
    .attr('stroke', 'black')
    .attr('stroke-width', 2);

  // Draw horizontal segment lines
  for (let i = 1; i < segments; i++) {
    svg.append('line')
      .attr('x1', x)
      .attr('x2', x + width)
      .attr('y1', y + i * segmentHeight)
      .attr('y2', y + i * segmentHeight)
      .attr('stroke', 'black')
      .attr('stroke-dasharray', '4,4')
      .attr('stroke-width', 0.5);
  }

  // Add Memory text above rectangle
  svg.append('text')
    .attr('x', x + width / 2)
    .attr('y', y / 2)
    .attr('text-anchor', 'middle')
    .attr('font-size', '20px')
    .text('Memory');

  // Add text beside rectangle
  const textData = [
    '// boolean = 1 byte',
    '// CHAR = 2 bytes',
    '// int, float = 4 bytes (default floating point in COMP1000)',
    '// double = 8 bytes (default floating point in COMP1000)',
  ];

  textData.forEach((line, i) => {
    const textX = text_x;
    const textY = 380;
    // Add lines of text
    svg.append('text')
      .attr('x', textX)
      .attr('y', textY + i * text_h)
      .attr('dominant-baseline', 'middle')
      .attr('font-size', '16px')
      .text(line);
  });


  // Data for segment animations
  const segmentsData = [
    {
      name: 'leftToRight',
      value: 'true',
      yStart: 5,
      span: 1,
      text: 'boolean leftToRight = true;',
    },
    {
      name: 'nStudents',
      value: '10',
      yStart: 0,
      span: 4,
      text: 'int nStudents = 10;',
    },
    {
      name: 'current',
      value: '4',
      yStart: 21,
      span: 4,
      text: 'int current = 4;',
    },
    {
      name: 'firstLetter',
      value: 'G',
      yStart: 19,
      span: 2,
      text: "char firstLetter = 'G';",
    },
    {
      name: 'approxPi',
      value: '3.14',
      yStart: 7,
      span: 4,
      text: 'float approxPi = 3.14;',
    },
    {
      name: 'betterPi',
      value: '3.1415926',
      yStart: 11,
      span: 8,
      text: 'double betterPi = 3.1415926;',
    },
    {
      name: 'current',
      value: '10',
      yStart: 21,
      span: 4,
      text: 'current = nStudents;',
    },
  ];

  // Add in rectangle segments
  function addSegmentAnimation(group, d, i) {
    const rectY = y + d.yStart * segmentHeight;
    const rectHeight = d.span * segmentHeight;
    const centerY = rectY + rectHeight / 2;
    const delay = i * delayStep;

    // Add line of text
    group.append("text")
      .attr("x", text_x)
      .attr("y", y + i * text_h)
      .attr("font-size", "16px")
      .text(d.text)
      .style("opacity", 0)
      .transition()
      .delay(delay)
      .duration(400)
      .style("opacity", 1);

    // Draw hollow rectangle with animation
    group.append("rect")
      .attr("x", x)
      .attr("y", rectY)
      .attr("width", width)
      .attr("height", rectHeight)
      .attr("fill", "none")
      .attr("stroke", "green")
      .attr("stroke-width", 4)
      .style("opacity", 0)
      .transition()
      .delay(delay + 400)
      .duration(400)
      .style("opacity", 1);

    // Draw value in rectangle center
    group.append("text")
      .attr("x", x + width / 2)
      .attr("y", centerY)
      .attr("text-anchor", "middle")
      .attr('dominant-baseline', 'middle')
      .attr("font-size", "14px")
      .text(d.value)
      .style("opacity", 0)
      .attr("class", d.name + "-value")
      .transition()
      .delay(delay + 800)
      .duration(300)
      .style("opacity", 1);

    //  Draw label on the right
    group.append("text")
      .attr("x", x + width + offset)
      .attr("y", centerY)
      .attr('dominant-baseline', 'middle')
      .attr("font-size", "16px")
      .attr("font-weight", "bold")
      .text(d.name)
      .style("opacity", 0)
      .transition()
      .delay(delay + 800)
      .duration(300)
      .style("opacity", 1);
  }

  // Function to animate the overwrite of an existing value with another existing value
  function animateReplacement(group, sourceIndex, destIndex, i){
    const delay = i * delayStep;
    const source = segmentsData[sourceIndex];
    const target = segmentsData[destIndex];

    const sourceY = y + source.yStart * segmentHeight + (source.span * segmentHeight) / 2;
    const targetY = y + target.yStart * segmentHeight + (target.span * segmentHeight) / 2;

    // Add line of code
    group.append("text")
      .attr("x", text_x)
      .attr("y", y + i * text_h)
      .attr("font-size", "16px")
      .text(target.text)
      .style("opacity", 0)
      .transition()
      .delay(delay)
      .duration(400)
      .style("opacity", 1);

    // Turn old value red then fade out
    group.selectAll("." + target.name + "-value")
      .transition()
      .delay(delay + 400)
      .duration(400)
      .attr("font-weight", "bold")
      .style("fill", "red")
      .transition()
      .delay(400)
      .duration(700)
      .style("opacity", 0);

    // Slide replacement value to target
    group.append("text")
      .attr("x", x + width / 2)
      .attr("y", sourceY)
      .attr("text-anchor", "middle")
      .attr("font-size", "14px")
      .text(source.value)
      .style("opacity", 0)
      .transition()
      .delay(delay + 800)
      .duration(400)
      .style('opacity', 1)
      .transition()
      .duration(400)
      .attr("y", targetY)
      .attr("dominant-baseline", "middle");

    // Restart
    setTimeout(() => {
      group.selectAll("*").remove();

      runAnimation();
    }, delay + 4000);
  }

  // Main animation function
  const animation = svg.append("g").attr("class", "animation-cycle");
  function runAnimation() {
    segmentsData.forEach((d, i) => {
      if (i < segmentsData.length - 1) {
        addSegmentAnimation(animation, d, i);
      } else {
        animateReplacement(animation, 1, 6, i);
      }
    });
  }

  runAnimation();

});
