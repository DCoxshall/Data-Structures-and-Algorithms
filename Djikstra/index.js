var grid = [];
var currentNode;
const SQUARE_SIZE = 20;

var FOUND = true;

var unvisited = [];

function setup() {
	createCanvas(500, 500);
	for (let i = 0; i < width; i += SQUARE_SIZE) {
		let newRow = [];
		for (let j = 0; j < width; j += SQUARE_SIZE) {
			newRow.push(new Square(i, j, SQUARE_SIZE));
		}
		grid.push(newRow);
	}
}

function mousePressed() {
	if (mouseX < 0 || mouseX > width || mouseY < 0 || mouseY > width) {
		return;
	}
	if (mouseButton == LEFT) {
		// Make sure there can only be one start and one finish

		for (let i = 0; i < grid.length; i++) {
			for (let j = 0; j < grid[0].length; j++) {
				if (grid[i][j].state == "start") {
					grid[i][j].setState("empty");
				}
			}
		}

		grid[Math.floor(mouseX / SQUARE_SIZE)][
			Math.floor(mouseY / SQUARE_SIZE)
		].setState("start");

		grid[Math.floor(mouseX / SQUARE_SIZE)][
			Math.floor(mouseY / SQUARE_SIZE)
		].distance = 0;
	} else {
		for (let i = 0; i < grid.length; i++) {
			for (let j = 0; j < grid[0].length; j++) {
				if (grid[i][j].state == "end") {
					grid[i][j].setState("empty");
				}
			}
		}
		grid[Math.floor(mouseX / SQUARE_SIZE)][
			Math.floor(mouseY / SQUARE_SIZE)
		].setState("end");
	}
}

function start_djikstra() {
	// Clear set of unvisited nodes
	unvisited = [];

	// Set all nodes apart from the starting node as unvisited
	for (let i = 0; i < grid.length; i++) {
		for (let j = 0; j < grid[0].length; j++) {
			if (grid[i][j].state == "start") {
				grid[i][j].distance = 0;
				currentNode = grid[i][j];
			} else if (grid[i][j].state == "end") {
				unvisited.push(grid[i][j]);
			} else if (grid[i][j].state != "wall") {
				unvisited.push(grid[i][j]);
				grid[i][j].setState("empty");
			}
		}
	}

	FOUND = false;
}

// Neighbours of (0, 0): [[0, 1], [1, 0]];
function pass() {
	if (unvisited.length == 0) {
		return;
	}
	let neighbours = currentNode.getNeighbours(grid);

	if (neighbours.length == 0) {
		// This would mean that there's no route between the start and end nodes
		FOUND = true;
		return;
	}

	for (let i = 0; i < neighbours.length; i++) {
		currentNeighbour = grid[neighbours[i][0]][neighbours[i][1]];
		currentNeighbour.distance = Math.min(
			currentNeighbour.distance,
			currentNode.distance + 1
		);
	}

	unvisited = unvisited.filter((item) => {
		return item != currentNode;
	});
	if (currentNode.state != "start" && currentNode.state != "end") {
		currentNode.setState("visited");
	}

	if (currentNode.state == "end") {
		traceBack();
		FOUND = true;
		return;
	} else {
		let shortestIndex;
		let shortest = 999999999;
		for (let i = 0; i < unvisited.length; i++) {
			if (unvisited[i].distance < shortest) {
				shortest = unvisited[i].distance;
				shortestIndex = i;
			}
		}
		currentNode = unvisited[shortestIndex];
	}
}

function traceBack() {
	console.log("traceback called");
	let finishNode;

	// Find start and end nodes, the reverse of the start and end nodes for djikstra
	for (let i = 0; i < grid.length; i++) {
		for (let j = 0; j < grid[0].length; j++) {
			if (grid[i][j].state == "end") {
				currentNode = grid[i][j];
			}
			if (grid[i][j].state == "start") {
				finishNode = grid[i][j];
			}
		}
	}

	while (currentNode != finishNode) {
		neighbours = currentNode.getNeighbours(grid);
		let closestNeighbour = currentNode;
		for (let i = 0; i < neighbours.length; i++) {
			currentNeighbour = grid[neighbours[i][0]][neighbours[i][1]];
			if (currentNeighbour.distance < closestNeighbour.distance) {
				closestNeighbour = currentNeighbour;
			}
		}
		closestNeighbour.setState("path");
		currentNode = closestNeighbour;
	}
	finishNode.setState("start");
}

function setWallAtCoords(x, y) {
	let i = Math.floor(x / SQUARE_SIZE);
	let j = Math.floor(y / SQUARE_SIZE);

	try {
		grid[i][j].setState("wall");
	} catch {}
}

function deleteWallAtCoords(x, y) {
	let i = Math.floor(x / SQUARE_SIZE);
	let j = Math.floor(y / SQUARE_SIZE);

	try {
		if (grid[i][j].state == "wall") {
			grid[i][j].setState("empty");
		}
	} catch {}
}

function draw() {
	background(51);
	for (let i = 0; i < grid.length; i++) {
		for (let j = 0; j < grid[0].length; j++) {
			grid[i][j].show();
		}
	}
	if (FOUND == false) {
		pass();
	}
	if (keyIsDown(87)) {
		if (keyIsDown(SHIFT)) {
			deleteWallAtCoords(mouseX, mouseY);
		} else {
			setWallAtCoords(mouseX, mouseY);
		}
	}
}
