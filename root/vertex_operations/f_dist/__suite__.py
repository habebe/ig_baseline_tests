name = "Distributed"
description = "Distributed Vertex Ingest/Query"

table_view = [
    [{"sTitle":"Version"},{"content":"object.engine()"}],
    [{"sTitle":"Platform"},{"content":"object.platform()"}],
    [{"sTitle":"Process"},{"content":"'T:%d'%(object.processes())"}],
    [{"sTitle":"Rate (v/s)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}]
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","object.processes()"),"xaxis":"Processes"},
        {"name":"time","data":("object.time_avg()","object.processes()"),"xaxis":"Processes"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        {"name":"Version","id":"object.engine_id()","content":"object.engine()"},
        {"name":"Index Type","id":"object.index_type_id()","content":"object.index_type()"},
        ]
    }

graph_size = pow(2,15)
query_size = pow(2,15)
tx_size = pow(2,14)
page_size = 14
cases = []
processes = [([0],1),([0,1],1)]

cases.append(
    {
    "name":"ingest",
    "description":"Vertex Ingestion as a function of hosts (page size=%d, transaction size=%d)"%(pow(2,page_size),tx_size),
    "type":"vertex_ingest",
    "data":
    {
    "template":["basic_non_unique"],
    "config":["dist_host:host1"],
    "page_size":[14],
    "threads":[1],
    "use_index":[0],
    "new":1,
    "txsize":[tx_size],
    "size":[graph_size],
    "ig_version":["ig.3.1","ig.3.0"],
    "process":processes,
    },
    "table_view":table_view,
    "plot_view":plot_view
    }
    )

