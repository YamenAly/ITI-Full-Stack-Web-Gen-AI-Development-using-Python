import { Rectangle,Square } from "./squaresModule.js";
import { Circle } from "./CircleModule.js";

const rect = new Rectangle("yellow", 10, 5);
const square = new Square("green", 5);
const circle = new Circle("red", 7, 0,0);


console.log("Rectangle Area:", rect.getArea());
console.log("Square Area:", square.getArea());
console.log("Circle Area:", circle.getArea());