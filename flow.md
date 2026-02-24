graph LR
    %% กำหนดสไตล์ของกล่อง
    classDef source fill:#d4edda,stroke:#28a745,stroke-width:2px;
    classDef queue fill:#fff3cd,stroke:#ffc107,stroke-width:2px;
    classDef delay fill:#cce5ff,stroke:#007bff,stroke-width:2px;
    classDef router fill:#e2e3e5,stroke:#6c757d,stroke-width:2px;
    classDef service fill:#f8d7da,stroke:#dc3545,stroke-width:2px;
    classDef sink fill:#343a40,stroke:#343a40,stroke-width:2px,color:#fff;
    classDef db fill:#6f42c1,stroke:#6f42c1,stroke-width:2px,color:#fff;

    %% Source
    Src["Source<br/>(จำลองผู้ใช้งาน)"]:::source --> Q["Queue<br/>(GatewayBuffer)<br/>Cap: 500"]:::queue

    %% Gateway Layer
    Q -- "Timeout" --> SinkTO["Sink<br/>(Sink_Drop_Timeout)"]:::sink
    Q --> Del["Delay<br/>(FastAPI_Process)<br/>+ Java Logic"]:::delay
    Del --> Rout{"SelectOutput5<br/>(Router)"}:::router

    %% Routing to Microservices
    Rout -- "Condition 1" --> SvcA["Service<br/>(Service_Reg)"]:::service
    Rout -- "Condition 2" --> SvcB["Service<br/>(Service_Contrib)"]:::service
    Rout -- "Condition 3" --> SvcC["Service<br/>(Service_Benefits)"]:::service
    Rout -- "Condition 4" --> SvcD["Service<br/>(Service_Accounting)"]:::service
    Rout -- "Default (Error)" --> SinkErr["Sink<br/>(Sink_Error_Route)"]:::sink

    %% Sinks (Success)
    SvcA --> SinkA["Sink<br/>(Sink_Success_A)"]:::sink
    SvcB --> SinkB["Sink<br/>(Sink_Success_B)"]:::sink
    SvcC --> SinkC["Sink<br/>(Sink_Success_C)"]:::sink
    SvcD --> SinkD["Sink<br/>(Sink_Success_D)"]:::sink

    %% Database Resource Pool
    subgraph Database Layer [PostgreSQL Database]
        DB[("ResourcePool<br/>(DB_Connections)<br/>Cap: 100")]:::db
    end

    %% Resource Dependency (Seize)
    DB -. "Seize / Release" .-> SvcA
    DB -. "Seize / Release" .-> SvcB
    DB -. "Seize / Release" .-> SvcC
    DB -. "Seize / Release" .-> SvcD