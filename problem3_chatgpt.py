import tkinter as tk
import math

class PolygonDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Polygon Drawer")
        
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()
        
        self.points = []
        self.labels = []
        self.lines = []
        self.polygon_drawn = False
        
        self.canvas.bind("<Button-1>", self.add_point)
        
        self.complete_button = tk.Button(root, text="Complete Polygon", command=self.complete_polygon)
        self.complete_button.pack()
        
        self.restart_button = tk.Button(root, text="Restart", command=self.restart)
        self.restart_button.pack()
        
        self.selected_label = None
        self.offset_x = 0
        self.offset_y = 0
        
        self.canvas.bind("<ButtonPress-3>", self.start_drag)
        self.canvas.bind("<B3-Motion>", self.drag_label)
    
    def add_point(self, event):
        if self.polygon_drawn:
            return
        x, y = event.x, event.y
        self.points.append((x, y))
        
        if len(self.points) > 1:
            line = self.canvas.create_line(self.points[-2], self.points[-1], fill="blue")
            self.lines.append(line)
        
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="red")
    
    def complete_polygon(self):
        if len(self.points) > 2:
            self.lines.append(self.canvas.create_line(self.points[-1], self.points[0], fill="blue"))
            self.canvas.create_polygon(self.points, outline="blue", fill="gray", tags="polygon")
            self.polygon_drawn = True
            self.label_points()
            self.calculate_metrics()
    
    def label_points(self):
        for x, y in self.points:
            label = self.canvas.create_text(x+5, y-5, text=f"({x},{y})", font=("Arial", 10), tags="label")
            self.labels.append(label)
    
    def calculate_metrics(self):
        perimeter = 0
        area = 0
        n = len(self.points)
        for i in range(n):
            x1, y1 = self.points[i]
            x2, y2 = self.points[(i + 1) % n]
            perimeter += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            area += (x1 * y2 - x2 * y1)
        area = abs(area) / 2
        
        self.canvas.create_text(300, 20, text=f"Perimeter: {perimeter:.2f}", font=("Arial", 12), tags="metrics")
        self.canvas.create_text(300, 40, text=f"Area: {area:.2f}", font=("Arial", 12), tags="metrics")
    
    def start_drag(self, event):
        closest = self.canvas.find_closest(event.x, event.y)[0]
        if "label" in self.canvas.gettags(closest):
            self.selected_label = closest
            self.offset_x = event.x - self.canvas.coords(closest)[0]
            self.offset_y = event.y - self.canvas.coords(closest)[1]
    
    def drag_label(self, event):
        if self.selected_label:
            self.canvas.coords(self.selected_label, event.x - self.offset_x, event.y - self.offset_y)
    
    def restart(self):
        self.canvas.delete("all")
        self.points.clear()
        self.labels.clear()
        self.lines.clear()
        self.polygon_drawn = False
    
if __name__ == "__main__":
    root = tk.Tk()
    app = PolygonDrawer(root)
    root.mainloop()
