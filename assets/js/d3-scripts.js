// For creating D3 images.

// This example generates a blue circle wherever you add the HTML id "my-d3-target".
document.addEventListener("DOMContentLoaded", function () {
    const el = document.getElementById("my-d3-target");
    if (!el) return;

    const svg = d3.select(el)
      .append("svg")
      .attr('viewBox', `0 0 300 200`)
      .attr('preserveAspectRatio', 'xMidYMid meet')
      .attr("width", 300)
      .attr("height", 200)
      .classed('responsive-svg', true);


    svg.append("circle")
      .attr("cx", 150)
      .attr("cy", 100)
      .attr("r", 50)
      .style("fill", "steelblue");
  });




/* For creating grids */

document.addEventListener("DOMContentLoaded", function () {
  const  cellSize = 20;

  // To draw the  grid base
  function drawGrid(svg, rows, cols, wOffset, hOffset) {
    const totalWidth = cols *  cellSize + wOffset;
    const totalHeight = rows * cellSize + hOffset;

    svg
    .attr('viewBox', `0 0 ${totalWidth} ${totalHeight}`)
    .attr('preserveAspectRatio', 'xMidYMid meet')
    .attr("width", totalWidth)
    .attr("height", totalHeight)
    .classed('responsive-svg', true);



    for (let y = 0; y < rows; y++) {
      for (let x = 0; x < cols; x++) {
        svg.append("rect")
          .attr("x", x *  cellSize)
          .attr("y", y *  cellSize)
          .attr("width",  cellSize)
          .attr("height",  cellSize)
          .attr("fill", "white")
          .attr("stroke", "black");
      }
    }
  }

  // To add values inside the grid
  function valuesToGrid(svg, numberData = []){
    numberData.forEach((d) => {
      if(d.text !== ""){
        svg.append("text")
        .attr("x", d.x *  cellSize +  cellSize / 2)
        .attr("y", d.y *  cellSize +  cellSize / 2)
        .attr("text-anchor", "middle")
        .attr("dominant-baseline", "middle")
        .attr("font-size", "12px")
        .text(d.text);
      }
    })
  }

  // To add a pointer
  function textPointer(svg, cols, textData){
    // Define arrow marker once
    svg.append("defs")
    .append("marker")
      .attr("id", "arrowhead")
      .attr("viewBox", "-5 -5 10 10")
      .attr("refX", 0)
      .attr("refY", 0)
      .attr("markerWidth", 6)
      .attr("markerHeight", 6)
      .attr("orient", "auto")
    .append("path")
      .attr("d", "M -10,-10 L 0,0 L -10,10")

    textData.forEach(data => {
    // Determine coordinates from given cell
    const cellX = data.x;
    const cellY = data.y;

    const pointPosX = cellX *  cellSize +  cellSize ;
    const pointPosY = cellY *  cellSize +  cellSize / 2;

    const xOffset = 25; // shift to left/right if needed
    const textPosX = cols *  cellSize + xOffset; // place text to the right the grid
    const textPosY = pointPosY;

    // Add text label
    svg.append("text")
    .attr("x", textPosX)
    .attr("y", textPosY)
    .attr("text-anchor", "start")
    .attr("dominant-baseline", "middle")
    .attr("font-size", "18px")
    .text(data.text);

    // Arrow from "x" to cell
    svg.append("line")
    .attr("x1", textPosX)
    .attr("y1", textPosY)
    .attr("x2", pointPosX)
    .attr("y2", pointPosY)
    .attr("stroke", "black")
    .attr("stroke-width", 2)
    .attr("marker-end", "url(#arrowhead)");
    })

  }

  // Grid 3: diagonal matrix
  const matrix = [
    ["1", "", "", "", "", "", "", "", ""],
    ["", "2", "", "", "", "", "", "", ""],
    ["", "", "3", "", "", "", "", "", ""],
    ["", "", "", "4", "", "", "", "", ""],
    ["", "", "", "", "5", "", "", "", ""],
    ["", "", "", "", "", "6", "", "", ""],
    ["", "", "", "", "", "", "7", "", ""],
    ["", "", "", "", "", "", "", "8", ""],
    ["", "", "", "", "", "", "", "", "9"]
  ];

  const matrixData = [];
  for (let y = 0; y < matrix.length; y++) {
    for (let x = 0; x < matrix[y].length; x++) {
      if (matrix[y][x]) {
        matrixData.push({ x, y, text: matrix[y][x] });
      }
    }
  }


  /* Generating all grids */
  // Get all grid elements
  const elements = document.getElementsByClassName("grid");
  if (!elements.length) return;

  Array.from(elements).forEach(el => {
    const id = el.id;
    const rows = parseInt(el.getAttribute("rows"), 10)
    const cols = parseInt(el.getAttribute("cols"), 10)

    const svg = d3.select(el)
      .append("svg")

    // Determine the offsets
    let wOffset = 0;
    let hOffset = 0;
    if (id === "x-5" || id === "solution-1" || id === "solution-2"){
      wOffset = 50;
    }
    // Draw the grid base
    drawGrid(svg, rows, cols, wOffset, hOffset);

    // Add extra text depending on id
    if (id === "1-15-rand") {
      // Placing "1" and "15" in random cells
      valuesToGrid(svg, [
        { x: Math.floor(Math.random() * cols), y: Math.floor(Math.random() * rows), text: "15" },
        { x: Math.floor(Math.random() * cols), y: Math.floor(Math.random() * rows), text: "1" }
      ]);
    }
    else if (id === "matrix-diag"){
      // A particular method to fill in data with a matrix
      valuesToGrid(svg, matrixData);
    }
    else if (id === "x-5"){
      // Randomise the cell to add "5" to and add a pointer for "x"
      const x = Math.floor(Math.random() * cols);
      const y = Math.floor(Math.random() * rows);

      valuesToGrid(svg,[{ x: x, y: y, text: "5" }])
      textPointer(svg, cols, [{ x: x, y: y, text: "x" }]);
    }
    else if (id === "solution-1"){
      const x1 = 0;
      const y1 = 0;
      const x2 = 0;
      const y2 = 1;
      valuesToGrid(svg, [
        { x: x1, y: y1, text: "15" },
        { x: x2, y: y2, text: "10" }
      ])
      textPointer(svg, cols, [
        { x: x1, y: y1, text: "x" },
        { x: x2, y: y2, text: "y" }
      ])
    }
    else if (id === "solution-2"){
      const x1 = 0;
      const y1 = 0;
      const x2 = 0;
      const y2 = 1;
      valuesToGrid(svg, [
        { x: x1, y: y1, text: "25" },
        { x: x2, y: y2, text: "25" }
      ])
      textPointer(svg, cols, [
        { x: x1, y: y1, text: "x" },
        { x: x2, y: y2, text: "y" }
      ])
    }
  });
});


