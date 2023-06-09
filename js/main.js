// 读取Excel文件并绘制图表
function renderChart(data) {
    // 使用 Map 来存储每天的论文数量
    const countsByDate = new Map()
    const countsByCategory = new Map()
    for (const row of data) {
        const date = row[2]
        const category = row[3]
        
        const count = countsByDate.get(date) || 0
        countsByDate.set(date, count + 1)
        
        const countByCategory = countsByCategory.get(category) || 0
        countsByCategory.set(category, countByCategory + 1)
    }

    // 将 Map 转换为两个数组：日期和论文数量
    const dates = Array.from(countsByDate.keys())
    const countsByDateArray = dates.map(date => countsByDate.get(date))
    // const counts = dates.map(date => countsByDate.get(date))

    const categories = Array.from(countsByCategory.keys())
    const countsByCategoryArray = categories.map(category => countsByCategory.get(category))

    // 获取页面元素和上下文
    const canvas1 = document.getElementById('chart1')
    const context1 = canvas1.getContext('2d')

    const canvas2 = document.getElementById('chart2')
    const context2 = canvas2.getContext('2d')

    // 设置图表的样式和数据
    const chart1 = new Chart(context1, {
        type: 'bar',
        data: {
            labels: dates,
            datasets: [{
                label: 'Paper Submissions Per Day',
                data: countsByDateArray,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    })

    const chart2 = new Chart(context2, {
        type: 'bar',
        data: {
            labels: categories,
            datasets: [{
                label: 'Category paper count (cumulative)',
                data: countsByCategoryArray,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    })


    // 监听日期条的拖动事件
    const dateRange1 = document.getElementById('date-range1')
    const dateRange2 = document.getElementById('date-range2')
    const dateDisplay = document.getElementById('date-display')

    dateRange1.addEventListener('input', event => {
        const index = event.target.value - 1
        chart1.data.datasets[0].data = countsByDateArray.slice(0, index + 1)
        chart1.update()
    })
    dateRange2.addEventListener('input', event => {
        const index = event.target.value - 1
        const selectedDate = dates[index]

        dateDisplay.textContent = selectedDate
    
        
        const rowsByDate = new Map()
        for (const row of data) {
            const date = row[2]
            if (!rowsByDate.has(date)) {
                rowsByDate.set(date, [])
            }
            rowsByDate.get(date).push(row)
        }

        // Compute cumulative counts for each category up to the selected date
        const countsByCategoryCumulative = new Map()
        for (const [date, rows] of rowsByDate) {
            if (date <= selectedDate) {
                for ( const row of rows) {
                    const category = row[3]
                    const cumulativeCount = countsByCategoryCumulative.get(category) || 0
                    countsByCategoryCumulative.set(category, cumulativeCount + 1)
                }
            }
        }
    
        // Convert cumulative counts Map to arrays for chart data
        const categoriesCumulative = Array.from(countsByCategoryCumulative.keys())
        const countsByCategoryCumulativeArray = categoriesCumulative.map(category => countsByCategoryCumulative.get(category))

        chart2.data.datasets[0].data = countsByCategoryCumulativeArray
        chart2.data.labels = categoriesCumulative
        chart2.update()
    })
    

    // 动态计算进度条的值
    const rangeMax = dates.length
    const rangeStep = 1
    dateRange1.setAttribute('max', rangeMax)
    dateRange1.setAttribute('step', rangeStep)
    dateRange1.value = rangeMax
    
    dateRange2.setAttribute('max', rangeMax)
    dateRange2.setAttribute('step', rangeStep)
    dateRange2.value = rangeMax
}

function renderCumChart(data) {
    const countsByDate = new Map()
    for (let i = 0; i < data.length; i++) {
        const row = data[i]
        const date = row[2]
        const count = countsByDate.get(date) || 0
        countsByDate.set(date, count + 1)
    }

    const dates = Array.from(countsByDate.keys())
    const counts = dates.map(date => countsByDate.get(date))

    const cumulativeCounts = counts.reduce((acc, val) => {
        acc.push(acc.length === 0 ? val : acc[acc.length - 1] + val)
        return acc
    }, [])

    const canvas = document.getElementById('chart3')
    const context = canvas.getContext('2d')

    const chart = new Chart(context, {
        type: 'bar',
        data: {
            labels: dates,
            datasets: [{
                label: 'Cumulative Paper Submissions',
                data: cumulativeCounts,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes :[{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    })

    const dateRange = document.getElementById('date-range3')
    const dateDisplay = document.getElementById('date-display2')

    dateRange.addEventListener('input', event => {
        const index = event.target.value - 1
        const selectedDate = dates[index]
        dateDisplay.textContent = selectedDate

        chart.data.datasets[0].data = cumulativeCounts.slice(0, index + 1)
        chart.update()
    })

    const rangeMax = dates.length
    const rangeStep = 1
    dateRange.setAttribute('max', rangeMax)
    dateRange.setAttribute('step', rangeStep)
    dateRange.value = rangeMax
}

// 读取Excel文件
function readExcelFile(url) {
    const request = new XMLHttpRequest()
    request.open('GET', url, true)
    request.responseType = 'arraybuffer'

    request.onload = function() {
        const data = new Uint8Array(request.response)
        const workbook = XLSX.read(data, {type: 'array'})
        const sheetName = workbook.SheetNames[0]
        const sheet = workbook.Sheets[sheetName]
        const range = XLSX.utils.decode_range(sheet['!ref'])
        const rows = []
        for (let i = range.s.r + 1; i <= range.e.r; i++) {
            const row = []
            for (let j = range.s.c; j <= range.e.c; j++) {
                const cell = sheet[XLSX.utils.encode_cell({r: i, c: j})]
                row.push(cell ? cell.v : undefined)
            }
            rows.push(row)
        }
        renderChart(rows)
        renderCumChart(rows)
    }
    request.send()
}

// 读取Excel文件并生成图表
readExcelFile('articles.xlsx')