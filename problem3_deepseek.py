import tkinter as tk
from tkinter import messagebox
import math

class PolygonDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Polygon Drawer")

        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()

        self.points = []
        self.labels = []
        self.polygon_completed = False  # Track if the polygon is completed

        # Label to display cursor position
        self.cursor_position_label = tk.Label(root, text="Cursor: (0, 0)", font=("Arial", 10))
        self.cursor_position_label.pack()

        # Label to display perimeter and area
        self.metrics_label = tk.Label(root, text="Perimeter: 0.00 | Area: 0.00", font=("Arial", 10), anchor="w")
        self.metrics_label.pack(side="bottom", fill="x")

        self.canvas.bind("<Button-1>", self.add_point)
        self.canvas.bind("<Motion>", self.update_cursor_position)

        self.complete_button = tk.Button(root, text="Complete Polygon", command=self.complete_polygon)
        self.complete_button.pack()

        self.clear_button = tk.Button(root, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack()

    def add_point(self, event):
        if self.polygon_completed:
            return  # Do not add points after the polygon is completed

        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="red")  # Draw a small red circle at the point

        if len(self.points) > 1:
            # Draw a blue line between the last two points
            self.canvas.create_line(self.points[-2], self.points[-1], fill="blue")

    def update_cursor_position(self, event):
        # Update the cursor position label
        self.cursor_position_label.config(text=f"Cursor: ({event.x}, {event.y})")

        if len(self.points) > 0 and not self.polygon_completed:
            # Show a preview line from the last point to the cursor
            self.canvas.delete("preview_line")
            self.canvas.create_line(self.points[-1], (event.x, event.y), fill="blue", dash=(4, 2), tag="preview_line")

    def complete_polygon(self):
        if len(self.points) < 3:
            messagebox.showwarning("Warning", "At least 3 points are required to draw a polygon.")
            return

        # Clear the preview line
        self.canvas.delete("preview_line")

        # Close the polygon by connecting the last point to the first
        self.canvas.create_line(self.points[-1], self.points[0], fill="blue")

        # Fill the polygon with gray
        self.canvas.create_polygon(self.points, fill="gray", outline="blue")

        # Label the coordinates of each point
        for i, (x, y) in enumerate(self.points):
            label = self.canvas.create_text(x, y, text=f"({x}, {y})", fill="black", font=("Arial", 8))
            self.labels.append(label)
            self.canvas.tag_bind(label, "<Button-3>", lambda event, lbl=label: self.start_drag(event, lbl))  # Right-click to drag
            self.canvas.tag_bind(label, "<B3-Motion>", lambda event, lbl=label: self.drag_label(event, lbl))

        # Calculate and display perimeter and area
        perimeter = self.calculate_perimeter()
        area = self.calculate_area()
        self.metrics_label.config(text=f"Perimeter: {perimeter:.2f} | Area: {area:.2f}")

        # Prevent adding new points after the polygon is completed
        self.polygon_completed = True
        self.canvas.unbind("<Button-1>")

    def calculate_perimeter(self):
        perimeter = 0.0
        for i in range(len(self.points)):
            x1, y1 = self.points[i]
            x2, y2 = self.points[(i + 1) % len(self.points)]  # Wrap around to the first point
            perimeter += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return perimeter

    def calculate_area(self):
        area = 0.0
        for i in range(len(self.points)):
            x1, y1 = self.points[i]
            x2, y2 = self.points[(i + 1) % len(self.points)]  # Wrap around to the first point
            area += (x1 * y2 - x2 * y1)
        return abs(area) / 2

    def start_drag(self, event, label):
        self.drag_data = {"x": event.x, "y": event.y, "label": label}

    def drag_label(self, event, label):
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        self.canvas.move(label, dx, dy)
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def clear_canvas(self):
        self.canvas.delete("all")
        self.points = []
        self.labels = []
        self.polygon_completed = False
        self.canvas.bind("<Button-1>", self.add_point)  # Re-enable adding points after clearing
        self.cursor_position_label.config(text="Cursor: (0, 0)")  # Reset cursor position label
        self.metrics_label.config(text="Perimeter: 0.00 | Area: 0.00")  # Reset metrics label

if __name__ == "__main__":
    root = tk.Tk()
    app = PolygonDrawer(root)
    root.mainloop()