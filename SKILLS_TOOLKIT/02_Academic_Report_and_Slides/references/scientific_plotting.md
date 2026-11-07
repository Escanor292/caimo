# Scientific & Academic Data Visualization

This manual covers production-grade scientific chart generation adhering to the publication standards of top journals and conferences (IEEE, Nature, Science, ACM).

---

## 1. SciencePlots (Matplotlib Styles for IEEE & Nature)

* **Repository:** [garrettj403/SciencePlots](https://github.com/garrettj403/SciencePlots)
* **Installation:** `pip install scienceplots`
* **Core Value:** Automatically applies professional typography (serif fonts / Computer Modern), academic color cycles, discrete tick marks, and compact axis layouts with a single command:
  ```python
  import matplotlib.pyplot as plt
  import scienceplots

  plt.style.use(['science', 'no-latex', 'grid']) # 'no-latex' allows running without system LaTeX
  ```

### Standard Academic Plot Recipe:

```python
import matplotlib.pyplot as plt
import numpy as np
import scienceplots

# Use IEEE/Nature clean styling
plt.style.use(['science', 'no-latex', 'grid'])

fig, ax = plt.subplots(figsize=(6, 4), dpi=300)

epochs = np.arange(1, 41)
train_loss = 0.8 * np.exp(-epochs / 8) + 0.1
val_loss = 0.85 * np.exp(-epochs / 10) + 0.18 + 0.02 * np.random.randn(40) * 0.2

ax.plot(epochs, train_loss, label='Training Loss', color='#0C5DA5', linewidth=1.8)
ax.plot(epochs, val_loss, label='Validation Loss', color='#FF2C00', linestyle='--', linewidth=1.8)

ax.set_xlabel('Epoch')
ax.set_ylabel('Cross-Entropy Loss')
ax.set_title('Neural Network Convergence (MLP - DT69)')
ax.legend(frameon=True, loc='upper right')
ax.autoscale(tight=True)

# Save in high-resolution vector (PDF) and raster (PNG)
plt.savefig('academic_loss_curve.png', dpi=300, bbox_inches='tight')
plt.savefig('academic_loss_curve.pdf', bbox_inches='tight')
plt.close()
```

### Style Combinations:
* `['science', 'ieee']`: Strict single/double-column dimensions for IEEE Transactions.
* `['science', 'nature']`: Nature journal palette with clean sans-serif/serif contrast.
* `['science', 'high-vis']`: High-contrast accessible color scheme for colorblind readers.
* `['science', 'notebook']`: Larger fonts suitable for PowerPoint presentation slides.

---

## 2. PlotNeuralNet (3D Deep Learning Architecture Visualizer)

* **Repository:** [HarisIqbal88/PlotNeuralNet](https://github.com/HarisIqbal88/PlotNeuralNet)
* **Best For:** Generating 3D layered architectural diagrams of Convolutional Networks, Autoencoders, and MLP pipelines in LaTeX / TikZ.
* **Key Components:**
  * `to_Conv`: Convolutional feature map box.
  * `to_Pool`: Pooling / downsampling layer.
  * `to_UnPool`: Upsampling layer.
  * `to_Dense`: Fully connected / linear projection layer.
  * `to_connection`: Skip connections, residual additions.

---

## 3. Apache ECharts (Rich Interactive Statistical Visualizations)

* **Repository:** [apache/echarts](https://github.com/apache/echarts)
* **Python Wrapper:** `pyecharts` (`pip install pyecharts`)
* **Best For:** Radar charts, Sankey flow diagrams, Sunburst hierarchies, and multi-metric comparisons for interactive web dashboards and slide captures.

### Multi-Metric Radar Chart for Model Comparison:
```python
from pyecharts.charts import Radar
from pyecharts import options as opts

radar = (
    Radar()
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="Độ chính xác (Accuracy)", max_=1.0),
            opts.RadarIndicatorItem(name="Macro F1-Score", max_=1.0),
            opts.RadarIndicatorItem(name="Khả năng giải thích", max_=1.0),
            opts.RadarIndicatorItem(name="Tốc độ suy luận", max_=1.0),
            opts.RadarIndicatorItem(name="Độ bền vững (Robustness)", max_=1.0),
        ]
    )
    .add("Random Forest", [[0.95, 0.90, 0.85, 0.92, 0.88]], color="#2b5c8f")
    .add("Mạng Nơ-ron (MLP)", [[0.88, 0.82, 0.40, 0.85, 0.80]], color="#d9534f")
    .add("Hệ chuyên gia Luật", [[0.82, 0.74, 1.00, 0.99, 0.70]], color="#5cb85c")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="So sánh Đa Tiêu chí các Giải pháp CTG"))
)
radar.render("model_radar_comparison.html")
```
