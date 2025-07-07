<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Guide: PRTG Data Analysis</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Chosen Palette: Warm Neutrals -->
    <!-- Application Structure Plan: The application is structured as a single-page, vertical-scrolling interactive guide. It translates the "how-to" nature of the source report into a learning journey. The flow is: 1. High-level architecture overview with interactive elements. 2. A showcase of the technology stack. 3. A live, hands-on dashboard demo simulating the end-product, which is the core interactive element. 4. A code explorer to view key implementation snippets. This structure was chosen to guide the user from concept to implementation, making the abstract process described in the report tangible and understandable. It prioritizes educational flow over a simple data dashboard. -->
    <!-- Visualization & Content Choices: Report Info -> Project Architecture, Goal: Organize/Inform, Viz/Method: Interactive flowchart using HTML/CSS Flexbox, Interaction: Click to reveal details, Justification: Visually explains the data flow process. | Report Info -> Tech Stack Table, Goal: Inform, Viz/Method: Interactive cards grid using HTML/Tailwind, Interaction: Click to see details, Justification: More engaging than a static table. | Report Info -> Core Dashboard Functionality, Goal: Compare/Change, Viz/Method: Chart.js line chart and HTML table, Interaction: Filtering data via checkboxes updates the chart and table dynamically, Justification: The most effective way to demonstrate the report's main goal—creating an interactive dashboard. | Report Info -> Code Examples, Goal: Inform, Viz/Method: Tabbed code snippets using HTML/JS, Interaction: Click tabs to switch code views, Justification: Allows users to inspect the "how" without leaving the page. -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->

    <style>
        body {
            font-family: 'Sarabun', sans-serif;
            background-color: #f8f9fa;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
            height: 40vh;
            max-height: 450px;
        }
        @media (max-width: 768px) {
            .chart-container {
                height: 50vh;
            }
        }
        .tab-btn {
            transition: all 0.3s ease;
        }
        .tab-btn.active {
            border-color: #0d9488;
            background-color: #ccfbf1;
            color: #134e4a;
            font-weight: 600;
        }
        .flow-step {
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        }
        .flow-step:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        }
    </style>
</head>
<body class="text-gray-800">

    <header class="bg-white shadow-sm sticky top-0 z-40">
        <div class="container mx-auto px-6 py-4">
            <h1 class="text-3xl font-bold text-teal-700">คู่มือเชิงโต้ตอบ: การวิเคราะห์ข้อมูล PRTG ด้วย Python</h1>
            <p class="text-gray-600 mt-1">แปลงรายงาน .html สู่ Dashboard ที่ใช้งานได้จริง</p>
        </div>
    </header>

    <main class="container mx-auto px-6 py-8">

        <section id="architecture" class="mb-16">
            <h2 class="text-2xl font-semibold mb-2">ภาพรวมสถาปัตยกรรม: จากข้อมูลดิบสู่ข้อมูลเชิงลึก</h2>
            <p class="text-gray-600 mb-8 max-w-3xl">หัวใจสำคัญของแอปพลิเคชันคือกระบวนการทำงานที่เป็นระบบและอัตโนมัติ 4 ขั้นตอน ตั้งแต่การรับข้อมูลไปจนถึงการส่งออกผลลัพธ์เพื่อนำไปใช้ต่อ คุณสามารถคลิกที่แต่ละขั้นตอนเพื่อดูคำอธิบายเพิ่มเติม</p>
            
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4 items-center">
                <div id="step-upload" class="flow-step bg-white p-4 rounded-lg shadow-md border-l-4 border-sky-500 text-center cursor-pointer">
                    <div class="text-4xl mb-2">📂</div>
                    <h3 class="font-semibold text-lg">1. อัปโหลด</h3>
                    <p class="text-sm text-gray-500">เริ่มต้นด้วยไฟล์ .html</p>
                </div>
                <div class="text-2xl text-center text-gray-400 hidden md:block">→</div>
                <div id="step-process" class="flow-step bg-white p-4 rounded-lg shadow-md border-l-4 border-amber-500 text-center cursor-pointer">
                    <div class="text-4xl mb-2">⚙️</div>
                    <h3 class="font-semibold text-lg">2. ประมวลผล</h3>
                    <p class="text-sm text-gray-500">สกัดและทำความสะอาด</p>
                </div>
                 <div class="text-2xl text-center text-gray-400 hidden md:block">→</div>
                 <div id="step-visualize" class="flow-step bg-white p-4 rounded-lg shadow-md border-l-4 border-emerald-500 text-center cursor-pointer">
                    <div class="text-4xl mb-2">📊</div>
                    <h3 class="font-semibold text-lg">3. แสดงผล</h3>
                    <p class="text-sm text-gray-500">สร้างกราฟและตาราง</p>
                </div>
                 <div class="text-2xl text-center text-gray-400 hidden md:block">→</div>
                 <div id="step-export" class="flow-step bg-white p-4 rounded-lg shadow-md border-l-4 border-violet-500 text-center cursor-pointer">
                    <div class="text-4xl mb-2">📥</div>
                    <h3 class="font-semibold text-lg">4. ส่งออก</h3>
                    <p class="text-sm text-gray-500">ดาวน์โหลดเป็น Excel/CSV</p>
                </div>
            </div>
            <div id="architecture-details" class="mt-6 bg-white p-6 rounded-lg shadow hidden">
                <h4 id="detail-title" class="font-bold text-teal-700 text-xl mb-2"></h4>
                <p id="detail-text" class="text-gray-700"></p>
            </div>
        </section>

        <section id="tech-stack" class="mb-16">
            <h2 class="text-2xl font-semibold mb-2">ชุดเครื่องมือและไลบรารี (Technology Stack)</h2>
            <p class="text-gray-600 mb-8 max-w-3xl">ความสำเร็จของโปรเจกต์นี้อาศัยไลบรารี Python แบบ Open-source ที่ทรงพลัง ซึ่งแต่ละตัวมีหน้าที่เฉพาะทางและทำงานร่วมกันได้อย่างลงตัว</p>
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                <div class="bg-white p-4 rounded-lg shadow-sm border hover:shadow-lg transition-shadow">
                    <h3 class="font-bold text-lg">Streamlit</h3>
                    <p class="text-sm text-gray-600">สร้างเว็บแอปฯ ข้อมูลอย่างรวดเร็วด้วย Python</p>
                </div>
                <div class="bg-white p-4 rounded-lg shadow-sm border hover:shadow-lg transition-shadow">
                    <h3 class="font-bold text-lg">Pandas</h3>
                    <p class="text-sm text-gray-600">เครื่องมือหลักในการจัดการและวิเคราะห์ข้อมูล</p>
                </div>
                <div class="bg-white p-4 rounded-lg shadow-sm border hover:shadow-lg transition-shadow">
                    <h3 class="font-bold text-lg">Plotly</h3>
                    <p class="text-sm text-gray-600">สร้างกราฟที่สวยงามและโต้ตอบได้</p>
                </div>
                <div class="bg-white p-4 rounded-lg shadow-sm border hover:shadow-lg transition-shadow">
                    <h3 class="font-bold text-lg">BeautifulSoup4</h3>
                    <p class="text-sm text-gray-600">แยกวิเคราะห์ข้อมูลจากไฟล์ HTML</p>
                </div>
                 <div class="bg-white p-4 rounded-lg shadow-sm border hover:shadow-lg transition-shadow">
                    <h3 class="font-bold text-lg">openpyxl</h3>
                    <p class="text-sm text-gray-600">สำหรับเขียนไฟล์ไปยังรูปแบบ Excel (.xlsx)</p>
                </div>
                 <div class="bg-white p-4 rounded-lg shadow-sm border hover:shadow-lg transition-shadow">
                    <h3 class="font-bold text-lg">python-pptx</h3>
                    <p class="text-sm text-gray-600">สร้างสไลด์ PowerPoint อัตโนมัติ (ฟีเจอร์อนาคต)</p>
                </div>
            </div>
        </section>

        <section id="live-demo" class="mb-16">
             <h2 class="text-2xl font-semibold mb-2">ทดลองใช้งาน Dashboard</h2>
             <p class="text-gray-600 mb-6 max-w-3xl">นี่คือการจำลอง Dashboard ที่สร้างขึ้น คุณสามารถใช้ตัวกรองด้านล่างเพื่อเลือกเซิร์ฟเวอร์ที่ต้องการแสดงผลบนกราฟได้แบบเรียลไทม์ ข้อมูลที่ใช้เป็นข้อมูลตัวอย่างเพื่อสาธิตการทำงาน</p>
            <div class="bg-white rounded-lg shadow-lg p-4 md:p-6">
                <div class="flex flex-col md:flex-row gap-6">
                    <aside class="w-full md:w-1/4 lg:w-1/5 border-r-0 md:border-r md:pr-6">
                        <h3 class="text-lg font-semibold mb-4">⚙️ ตัวกรองข้อมูล</h3>
                        <div id="server-filters" class="space-y-2">
                        </div>
                         <button id="load-data-btn" class="mt-4 w-full bg-teal-600 text-white font-semibold py-2 px-4 rounded-lg hover:bg-teal-700 transition-colors">จำลองการอัปโหลดข้อมูล</button>
                    </aside>

                    <main class="w-full md:w-3/4 lg:w-4/5">
                        <div id="dashboard-content" class="hidden">
                            <div class="border-b border-gray-200">
                                <nav id="metric-tabs" class="flex space-x-2" aria-label="Tabs">
                                    <button data-tab="cpu" class="tab-btn active px-4 py-2 text-sm font-medium text-gray-500 rounded-t-lg border-b-2 border-transparent hover:text-gray-700 hover:border-gray-300">CPU Load (%)</button>
                                    <button data-tab="memory" class="tab-btn px-4 py-2 text-sm font-medium text-gray-500 rounded-t-lg border-b-2 border-transparent hover:text-gray-700 hover:border-gray-300">Memory Usage (%)</button>
                                </nav>
                            </div>
                            <div class="mt-4">
                                <div id="chart-container-wrapper">
                                     <div class="chart-container">
                                        <canvas id="performanceChart"></canvas>
                                    </div>
                                </div>
                               
                                <div class="mt-8">
                                     <details class="bg-gray-50 p-3 rounded-lg">
                                        <summary class="font-semibold cursor-pointer">แสดง/ซ่อน ตารางข้อมูลดิบ</summary>
                                        <div class="mt-4 overflow-x-auto">
                                            <table class="min-w-full divide-y divide-gray-200">
                                                <thead class="bg-gray-100">
                                                    <tr id="table-header"></tr>
                                                </thead>
                                                <tbody id="table-body" class="bg-white divide-y divide-gray-200">
                                                </tbody>
                                            </table>
                                        </div>
                                    </details>
                                </div>
                            </div>
                        </div>
                        <div id="dashboard-placeholder" class="text-center py-16 px-6">
                            <div class="text-5xl mb-4">📈</div>
                            <h3 class="text-xl font-semibold text-gray-700">รอข้อมูล...</h3>
                            <p class="text-gray-500">กรุณากดปุ่ม "จำลองการอัปโหลดข้อมูล" เพื่อเริ่มต้น</p>
                        </div>
                    </main>
                </div>
            </div>
        </section>

        <section id="code-explorer" class="mb-16">
            <h2 class="text-2xl font-semibold mb-2">สำรวจโค้ดหลัก (Code Explorer)</h2>
            <p class="text-gray-600 mb-6 max-w-3xl">ดูตัวอย่างโค้ด Python ที่เป็นหัวใจสำคัญในการทำงานแต่ละส่วน ตั้งแต่การแยกวิเคราะห์ HTML ไปจนถึงการสร้างกราฟ</p>
             <div class="bg-white rounded-lg shadow-lg">
                <div class="border-b border-gray-200">
                    <nav id="code-tabs" class="flex flex-wrap -mb-px" aria-label="Code Tabs">
                       <button data-code="parse" class="tab-btn active px-4 py-3 text-sm font-medium border-b-2">การแยกวิเคราะห์ (Parse)</button>
                       <button data-code="clean" class="tab-btn px-4 py-3 text-sm font-medium border-b-2">การทำความสะอาด (Clean)</button>
                       <button data-code="chart" class="tab-btn px-4 py-3 text-sm font-medium border-b-2">การสร้างกราฟ (Chart)</button>
                    </nav>
                </div>
                <div class="p-4 md:p-6 bg-gray-800 text-white rounded-b-lg overflow-x-auto">
                    <pre><code id="code-display" class="language-python text-sm"></code></pre>
                </div>
            </div>
        </section>
        
    </main>
    
    <footer class="bg-white mt-16 py-6 border-t">
        <div class="container mx-auto text-center text-gray-500">
            <p>สร้างสรรค์เป็นเว็บแอปพลิเคชันเชิงโต้ตอบเพื่อการเรียนรู้</p>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const performanceChartCanvas = document.getElementById('performanceChart');
            let performanceChart;
            let rawData = [];
            let currentMetric = 'cpu'; 
            
            const mockData = {
                cpu: [],
                memory: []
            };

            const serverNames = [
                'PROD-DB-01', 'PROD-WEB-01', 'PROD-API-01', 
                'UAT-DB-01', 'UAT-WEB-01', 'DEV-SERVER-01'
            ];
            
            function generateMockData() {
                const baseTime = new Date('2024-01-15T10:00:00Z').getTime();
                serverNames.forEach(server => {
                    let lastCpu = 5 + Math.random() * 20;
                    let lastMem = 20 + Math.random() * 30;
                    for (let i = 0; i < 60; i++) {
                        const timestamp = new Date(baseTime + i * 60 * 1000);
                        
                        lastCpu += (Math.random() - 0.5) * 5;
                        lastCpu = Math.max(5, Math.min(95, lastCpu));
                        mockData.cpu.push({
                            Timestamp: timestamp,
                            Value: lastCpu,
                            Server: server
                        });

                        lastMem += (Math.random() - 0.5) * 4;
                        lastMem = Math.max(20, Math.min(80, lastMem));
                        mockData.memory.push({
                            Timestamp: timestamp,
                            Value: lastMem,
                            Server: server
                        });
                    }
                });
            }

            function initChart() {
                if (performanceChart) {
                    performanceChart.destroy();
                }
                const ctx = performanceChartCanvas.getContext('2d');
                performanceChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        datasets: []
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            x: {
                                type: 'time',
                                time: {
                                    unit: 'minute',
                                    tooltipFormat: 'MMM d, yyyy, h:mm:ss a',
                                    displayFormats: {
                                        minute: 'h:mm a'
                                    }
                                },
                                title: {
                                    display: true,
                                    text: 'เวลา'
                                }
                            },
                            y: {
                                beginAtZero: true,
                                title: {
                                    display: true,
                                    text: 'ค่า (%)'
                                }
                            }
                        },
                        plugins: {
                            legend: {
                                position: 'top',
                            },
                            tooltip: {
                                mode: 'index',
                                intersect: false,
                            }
                        },
                        interaction: {
                            mode: 'nearest',
                            axis: 'x',
                            intersect: false
                        }
                    }
                });
            }
            
            function updateChart(filteredData) {
                if (!performanceChart) return;
                
                const selectedServers = Array.from(document.querySelectorAll('#server-filters input:checked')).map(el => el.value);

                const datasets = selectedServers.map((server, index) => {
                    const serverData = filteredData.filter(d => d.Server === server);
                    const colors = ['#3498db', '#e74c3c', '#2ecc71', '#f1c40f', '#9b59b6', '#1abc9c'];
                    return {
                        label: server,
                        data: serverData.map(d => ({ x: d.Timestamp, y: d.Value.toFixed(2) })),
                        borderColor: colors[index % colors.length],
                        backgroundColor: colors[index % colors.length] + '33',
                        fill: false,
                        tension: 0.1,
                        borderWidth: 2,
                        pointRadius: 1,
                        pointHoverRadius: 5
                    };
                });
                
                performanceChart.data.datasets = datasets;
                performanceChart.options.scales.y.title.text = `${currentMetric.toUpperCase()} Usage (%)`;
                performanceChart.update();
            }
            
            function updateTable(filteredData) {
                const tableHeader = document.getElementById('table-header');
                const tableBody = document.getElementById('table-body');

                tableHeader.innerHTML = `
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Timestamp</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Server</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">${currentMetric.toUpperCase()} (%)</th>
                `;
                
                let tableRows = '';
                const displayData = filteredData.slice(0, 100);
                displayData.forEach(d => {
                    tableRows += `
                        <tr>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${d.Timestamp.toLocaleString('th-TH')}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${d.Server}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${d.Value.toFixed(2)}</td>
                        </tr>
                    `;
                });
                tableBody.innerHTML = tableRows;
            }

            function refreshData() {
                const selectedServers = Array.from(document.querySelectorAll('#server-filters input:checked')).map(el => el.value);
                const dataForMetric = mockData[currentMetric];
                const filteredData = dataForMetric.filter(d => selectedServers.includes(d.Server));
                
                updateChart(filteredData);
                updateTable(filteredData);
            }

            function setupFilters() {
                const filterContainer = document.getElementById('server-filters');
                filterContainer.innerHTML = serverNames.map((name, index) => `
                    <label for="server-${index}" class="flex items-center space-x-2 cursor-pointer">
                        <input type="checkbox" id="server-${index}" value="${name}" class="h-4 w-4 rounded border-gray-300 text-teal-600 focus:ring-teal-500" ${index < 3 ? 'checked' : ''}>
                        <span class="text-sm text-gray-700">${name}</span>
                    </label>
                `).join('');
                
                filterContainer.addEventListener('change', refreshData);
            }

            document.getElementById('load-data-btn').addEventListener('click', () => {
                document.getElementById('dashboard-placeholder').classList.add('hidden');
                document.getElementById('dashboard-content').classList.remove('hidden');
                generateMockData();
                setupFilters();
                initChart();
                refreshData();
            });

            document.getElementById('metric-tabs').addEventListener('click', (e) => {
                if(e.target.tagName === 'BUTTON'){
                    const tab = e.target.dataset.tab;
                    if(tab !== currentMetric){
                        currentMetric = tab;
                        document.querySelectorAll('#metric-tabs .tab-btn').forEach(btn => btn.classList.remove('active'));
                        e.target.classList.add('active');
                        refreshData();
                    }
                }
            });
            
            const codeSnippets = {
                parse: `
import pandas as pd

def parse_prtg_table(html_file):
    """
    แยกวิเคราะห์ตารางข้อมูล Historic Data 
    จากไฟล์ HTML ของ PRTG
    """
    try:
        # ใช้ attrs เพื่อระบุตารางเป้าหมายอย่างแม่นยำ
        # สมมติว่าตารางมี class="table-historicdata"
        list_of_dfs = pd.read_html(
            html_file, 
            attrs={'class': 'table-historicdata'},
            flavor='lxml' # ใช้ lxml parser เพื่อประสิทธิภาพ
        )
        if list_of_dfs:
            return list_of_dfs[0]
        return None
    except Exception as e:
        print(f"ไม่สามารถประมวลผลไฟล์: {e}")
        return None
                `,
                clean: `
def clean_and_transform_df(df):
    """
    ทำความสะอาดและแปลงข้อมูลใน DataFrame
    """
    # เปลี่ยนชื่อคอลัมน์ให้ง่ายต่อการใช้งาน
    df = df.rename(columns={'Date Time': 'Timestamp'})

    # แปลง Timestamp เป็น datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], 
                                     errors='coerce')

    # ทำความสะอาดคอลัมน์ Value
    if 'Value' in df.columns:
        df['Value_Numeric'] = df['Value'].astype(str) \\
            .str.extract(r'(\\d+\\.?\\d*)').astype(float)
    
    df = df.dropna(subset=['Timestamp', 'Value_Numeric'])
    
    return df
                `,
                chart: `
import plotly.express as px

def create_performance_chart(data, metric_column, title):
    """สร้างกราฟเส้นด้วย Plotly Express"""
    fig = px.line(
        data,
        x='Timestamp',
        y=metric_column,
        color='Source VM', # สร้างเส้นกราฟแยกตาม VM
        title=title
    )
    fig.update_layout(legend_title_text='VM/Server')
    return fig

# การใช้งานใน Streamlit
# st.plotly_chart(fig, use_container_width=True)
                `
            };
            
            const codeDisplay = document.getElementById('code-display');
            const codeTabs = document.getElementById('code-tabs');
            
            codeDisplay.textContent = codeSnippets.parse.trim();

            codeTabs.addEventListener('click', (e) => {
                if (e.target.tagName === 'BUTTON') {
                    const codeKey = e.target.dataset.code;
                    codeDisplay.textContent = codeSnippets[codeKey].trim();
                    
                    document.querySelectorAll('#code-tabs .tab-btn').forEach(btn => btn.classList.remove('active'));
                    e.target.classList.add('active');
                }
            });

            const archDetails = {
                upload: {
                    title: '1. การอัปโหลด (Upload)',
                    text: 'ผู้ใช้เริ่มต้นด้วยการอัปโหลดไฟล์รายงาน PRTG ที่บันทึกไว้ในรูปแบบ .html (Webpage, HTML only) จำนวนหนึ่งหรือหลายร้อยไฟล์เข้าสู่เว็บแอปพลิเคชัน'
                },
                process: {
                    title: '2. การประมวลผล (Process)',
                    text: 'กลไกหลักของแอปพลิเคชันจะอ่านไฟล์ HTML, ใช้ตัวแยกวิเคราะห์ (Parser) เพื่อดึงข้อมูลจากตาราง, ทำการล้างข้อมูล (Cleaning) และสุดท้ายคือการรวมข้อมูลจากทุกไฟล์ให้กลายเป็นชุดข้อมูลหลัก (Master DataFrame) เพียงชุดเดียว'
                },
                visualize: {
                    title: '3. การแสดงผล (Visualize)',
                    text: 'ข้อมูลที่สะอาดแล้ว จะถูกนำไปแสดงผลบน Dashboard ในรูปแบบที่โต้ตอบได้ (Interactive) ซึ่งประกอบด้วยตารางข้อมูลที่ค้นหาได้ และกราฟเส้นที่แสดงแนวโน้มของเมตริกต่างๆ ผู้ใช้สามารถกรองข้อมูลเพื่อดูเฉพาะเซิร์ฟเวอร์ที่สนใจได้'
                },
                export: {
                    title: '4. การส่งออก (Export)',
                    text: 'ผู้ใช้สามารถดาวน์โหลดข้อมูลที่ประมวลผลแล้วในรูปแบบไฟล์ยอดนิยมอย่าง CSV หรือ Excel (.xlsx) ได้ด้วยการคลิกเพียงครั้งเดียว เพื่อนำไปวิเคราะห์ต่อหรือสร้างรายงานเพิ่มเติม'
                }
            };

            const detailContainer = document.getElementById('architecture-details');
            const detailTitle = document.getElementById('detail-title');
            const detailText = document.getElementById('detail-text');

            document.querySelectorAll('.flow-step').forEach(step => {
                step.addEventListener('click', () => {
                    const stepId = step.id.split('-')[1]; 
                    detailTitle.textContent = archDetails[stepId].title;
                    detailText.textContent = archDetails[stepId].text;
                    detailContainer.classList.remove('hidden');

                    document.querySelectorAll('.flow-step').forEach(s => s.classList.remove('ring-2', 'ring-teal-500'));
                    step.classList.add('ring-2', 'ring-teal-500');
                });
            });

        });
    </script>
</body>
</html>
