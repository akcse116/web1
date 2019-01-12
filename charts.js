// ******** Main Functions ********

// ******** HOME Page ********

// Upcoming Table

function ajaxPostEmail(data){
 var request = new XMLHttpRequest();
 request.open("POST", "/submit");
 request.send(data);
}


function upcoming_table(){
    var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function(){
            if (this.readyState === 4 && this.status === 200){
                var launch_data = get_vals_upcoming(this.response);
                Plotly.plot('upcoming_chart', launch_data.upcoming_launches, launch_data.layout);
            }
        };
        xhttp.open("GET", "/upcoming");
        xhttp.send();
}

function past_table(){
    var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function(){
            if (this.readyState === 4 && this.status === 200){
                var launch_data = get_vals_past(this.response);
                Plotly.plot('past_chart', launch_data.upcoming_launches, launch_data.layout);
            }
        };
        xhttp.open("GET", "/past");
        xhttp.send();
}

// Latest Table
function latest_table(){
    var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function(){
            if (this.readyState === 4 && this.status === 200){
                var launch_data = get_vals_latest(this.response);
                Plotly.plot('latest_chart', launch_data.upcoming_launches, launch_data.layout);
            }
        };
        xhttp.open("GET", "/latest");
        xhttp.send();
}

// ******** All Launches Page ********
function all_past_table(){
    var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function(){
            if (this.readyState === 4 && this.status === 200){
                var launch_data = get_vals_allPast(this.response);
                Plotly.plot('allPast_chart', launch_data.upcoming_launches, launch_data.layout);
            }
        };
        xhttp.open("GET", "/allPast");
        xhttp.send();
}


function site_pie(){
    var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function(){
            if (this.readyState === 4 && this.status === 200){
                var pie_data = launch_site_pie(this.response);
                console.log("data:" + pie_data);
                Plotly.plot('site_pie_chart', pie_data.data, pie_data.layout);
            }
        };
        xhttp.open("GET", "/site_count");
        xhttp.send();
}

// ******** Failed Launches Page ********


function all_failed_table(){
    var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function(){
            if (this.readyState === 4 && this.status === 200){
                var launch_data = get_vals_allPast_failed(this.response);
                Plotly.plot('fail_chart', launch_data.upcoming_launches, launch_data.layout);
            }
        };
        xhttp.open("GET", "/failed");
        xhttp.send();
}

// ********  Supporting Functions ********

function data_sort(raw_data){
    var result = [ [], [], [], [], [], [], [], [], []];
    for (var x of raw_data){
        result[0].push(String(x[0]));
        result[1].push(String(x[1]));
        result[2].push(String(x[2]));
        result[3].push(String(x[3]));
        result[4].push(String(x[4]));
        result[5].push(String(x[5]));
        result[6].push(String(x[6]));
        result[7].push(String(x[7]));
        result[8].push(String(x[8]));
    }
    return result; 
}


// Sorting for fail table (additional list in result)
function data_sort_2(raw_data){
    var result = [ [], [], [], [], [], [], [], [], [], []];
    for (var x of raw_data){
        result[0].push(String(x[0]));
        result[1].push(String(x[1]));
        result[2].push(String(x[2]));
        result[3].push(String(x[3]));
        result[4].push(String(x[4]));
        result[5].push(String(x[5]));
        result[6].push(String(x[6]));
        result[7].push(String(x[7]));
        result[8].push(String(x[8]));
        result[9].push(String(x[9]));
    }
    return result; 
}


function get_vals_upcoming(json){
    var data = JSON.parse(json);
    var cell_vals = data_sort(data);
    var launch_data = {
        upcoming_launches: [{
            type: 'table',
            columnwidth: [6, 30, 12, 34, 20, 20, 20, 30, 40],
            header: {
                values: [["#"], ["Mission Name"], ["Video"], ["Launch Date"], ["Vehicle"],
                			["Cargo"], ["Weight"], ["Cargo Owner"], ["Launch Site"]],
                align: "center",
                height: 40,
                line: {width: 4, color: 'black'},
                fill: {color: "#ffb200"},
                font: {family: "Arial", size: 18, color: "white"}
            },
            cells: {
                values: cell_vals,
                align: "center",
                height: 30,
                line: {color: "black", width: 4},
                fill: {color: "#666699"},
                font: {family: "Arial", size: 14, color: ["white"]}
            }
        }],
        layout: {
            title: 'Next 10 Launches',
            autosize: true,
            height: 700,
            margin: {
                l: 10,
                r: 10,
                b: 10,
                t: 50,
                pad: 0
            },
            paper_bgcolor: '#000000',
            plot_bgcolor: '#000000'
        }
    };
    return launch_data;
}

function get_vals_past(json){
    var data = JSON.parse(json);
    var cell_vals = data_sort(data);
    var launch_data = {
        upcoming_launches: [{
            type: 'table',
            columnwidth: [6, 30, 12, 34, 20, 20, 20, 30, 40],
            header: {
                values: [["#"], ["Mission Name"], ["Video"], ["Launch Date"], ["Vehicle"],
                			["Cargo"], ["Weight"], ["Cargo Owner"], ["Launch Site"]],
                align: "center",
                height: 40,
                line: {width: 4, color: 'black'},
                fill: {color: "#ffb200"},
                font: {family: "Arial", size: 18, color: "white"}
            },
            cells: {
                values: cell_vals,
                align: "center",
                height: 30,
                line: {color: "black", width: 4},
                fill: {color: "#666699"},
                font: {family: "Arial", size: 14, color: ["white"]}
            }
        }],
        layout: {
            title: 'Last 10 Launches',
            autosize: true,
            height: 740,
            margin: {
                l: 10,
                r: 10,
                b: 10,
                t: 50,
                pad: 0
            },
            paper_bgcolor: '#000000',
            plot_bgcolor: '#000000'
        }
    };
    return launch_data;
}


function get_vals_latest(json){
    var data = JSON.parse(json);
    var cell_vals = data_sort(data);
    var launch_data = {
        upcoming_launches: [{
            type: 'table',
            columnwidth: [6, 30, 12, 34, 20, 20, 20, 30, 40],
            header: {
                values: [["#"], ["Mission Name"], ["Video"], ["Launch Date"], ["Vehicle"],
                			["Cargo"], ["Weight"], ["Cargo Owner"], ["Launch Site"]],
                align: "center",
                height: 40,
                line: {width: 4, color: 'black'},
                fill: {color: "#ffb200"},
                font: {family: "Arial", size: 18, color: "white"}
            },
            cells: {
                values: cell_vals,
                align: "center",
                height: 60,
                line: {color: "black", width: 4},
                fill: {color: "#666699"},
                font: {family: "Arial", size: 14, color: ["white"]}
            }
        }],
        layout: {
            title: 'Latest SpaceX Mission',
            title_color: "#f2f2f2",
            autosize: true,
            height: 180,
            margin: {
                l: 10,
                r: 10,
                b: 10,
                t: 50,
                pad: 0
            },
            paper_bgcolor: '#000000',
            plot_bgcolor: '#000000'
        }
    };
    return launch_data;
}


function get_vals_allPast(json){
    var data = JSON.parse(json);
    var cell_vals = data_sort(data);
    var launch_data = {
        upcoming_launches: [{
            type: 'table',
            columnwidth: [6, 30, 12, 40, 20, 30, 20, 30, 40],
            header: {
                values: [["#"], ["Mission Name"], ["Video"], ["Launch Date"], ["Vehicle"],
                			["Cargo"], ["Weight"], ["Cargo Owner"], ["Launch Site"]],
                align: "center",
                height: 40,
                line: {width: 4, color: 'black'},
                fill: {color: "#ffb200"},
                font: {family: "Arial", size: 18, color: "white"}
            },
            cells: {
                values: cell_vals,
                align: "center",
                height: 30,
                line: {color: "black", width: 4},
                fill: {color: "#666699"},
                font: {family: "Arial", size: 14, color: ["white"]}
            }
        }],
        layout: {
            title: 'Full Launch Mission History     (Scroll to see all)',
            autosize: true,
            height: 4500,
            margin: {
                l: 10,
                r: 10,
                b: 10,
                t: 50,
                pad: 0
            },
            paper_bgcolor: '#000000',
            plot_bgcolor: '#000000'
        }
    };
    return launch_data;
}


function get_vals_allPast_failed(json){
    var data = JSON.parse(json);
    var cell_vals = data_sort_2(data);
    var launch_data = {
        upcoming_launches: [{
            type: 'table',
            columnwidth: [6, 30, 12, 40, 20, 20, 20, 30, 30, 100],
            header: {
                values: [["#"], ["Mission Name"], ["Video"], ["Launch Date"], ["Vehicle"],
                			["Cargo"], ["Weight"], ["Cargo Owner"], ["Launch Site"], ["Details"]],
                align: "center",
                height: 40,
                line: {width: 4, color: 'black'},
                fill: {color: "#ffb200"},
                font: {family: "Arial", size: 18, color: "white"}
            },
            cells: {
                values: cell_vals,
                align: "center",
                height: 30,
                line: {color: "black", width: 4},
                fill: {color: "#666699"},
                font: {family: "Arial", size: 14, color: ["white"]}
            }
        }],
        layout: {
            title: 'Failed Missions',
            autosize: true,
            height: 520,
            margin: {
                l: 10,
                r: 10,
                b: 10,
                t: 50,
                pad: 0
            },
            paper_bgcolor: '#000000',
            plot_bgcolor: '#000000'
        }
    };
    return launch_data;
}

function site_count(data){
    
}


function launch_site_pie(json){
    var data = JSON.parse(json);
    var cell_val = data;
    var pie = {
        data: [{
            values: cell_val,
            labels: ['Kwajalein Atoll Omelek Island', 
                'Cape Canaveral Air Force Station Space Launch Complex 40', 
              'Vandenberg Air Force Base Space Launch Complex 4E', 
              'Kennedy Space Center Historic Launch Complex 39A'],
            type: 'pie'
        }],
        layout: {
            title: 'Utilized Launch Sites',
            autosize: true,
            height: 600,
            width: 1000,
            color: 'white',
            margin: {
                l: 20,
                r: 140,
                b: 80,
                t: 80,
                pad: 0
            },
            paper_bgcolor: '#000000',
            plot_bgcolor: '#000000'
        }
    }
    return pie;
}