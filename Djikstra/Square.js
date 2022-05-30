class Square {
	constructor(initX, initY, initSize) {
		// Graphical attributes
		this.x = initX;
		this.y = initY;
		this.size = initSize;

		// Calculate distance from the start node
		this.distance = Infinity;

		// Can be one of the keys in colourMap, represents what the square actually is
		this.state = "empty";

		this.colourMap = {
			visited: color(150),
			path: color(0, 0, 255),
			end: color(255, 0, 0),
			start: color(0, 255, 0),
			empty: color(200),
			wall: color(255, 100, 0),
		};
	}

	show() {
		stroke(1);

		fill(this.colourMap[this.state]);

		rect(this.x, this.y, SQUARE_SIZE);

		// Uncomment this line for debugging, shows the distance from the start node
		text(this.state, this.x, this.y + this.size - 2);
	}

	// Returns the grid index of the neighbours of a given cell
	// Does not return neighbours if the neighbour is a wall
	getNeighbours(grid) {
		let neighbours = [];

		let logicalX = Math.floor(this.x / this.size);
		let logicalY = Math.floor(this.y / this.size);

		if (logicalX > 0) {
			if (grid[logicalX - 1][logicalY].state != "wall") {
				neighbours.push([logicalX - 1, logicalY]);
			}
		}
		if (logicalX < grid[0].length - 1) {
			if (grid[logicalX + 1][logicalY].state != "wall") {
				neighbours.push([logicalX + 1, logicalY]);
			}
		}
		if (logicalY > 0) {
			if (grid[logicalX][logicalY - 1].state != "wall") {
				neighbours.push([logicalX, logicalY - 1]);
			}
		}
		if (logicalY < grid.length - 1) {
			if (grid[logicalX][logicalY + 1].state != "wall") {
				neighbours.push([logicalX, logicalY + 1]);
			}
		}

		return neighbours;
	}

	setState(newState) {
		this.state = newState;
		if (this.state == "wall") {
			this.distance = Infinity;
		}
		if (this.state == "start") {
			this.distance = 0;
		}
		if (this.state == "empty") {
			this.distance = Infinity;
		}
	}
}
