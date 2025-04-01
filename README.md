# Awesome-CS-Conferences
Conferences about mobile systems, computer networks, operating systems


```mermaid
%%{init: {'theme': 'forest',
'themeVariables': { 'fontSize': '12px', 'fontFamily': 'sans-serif'},
"gantt": {
      "fontSize": 14,
      "sectionFontSize": 14
  }}}%%
gantt
    dateFormat  YYYY-MM-DD
    title Target Conferences (예시: 2025~2026)

    %% --------------------------
    %% Mobile
    %% --------------------------
    section Mobile
    MobiSys* (Submission)       :ms-sub,    2025-03-18, 7d
                              :ms-pres,   after ms-sub, 2d
    MobiCom* (Submission)       :mc-sub,    2025-11-14, 7d
    MobiCom* (Presentation)     :mc-pres,   after mc-sub, 2d
    UbiComp (Submission)        :ubi-sub,   2025-09-19, 7d
    UbiComp (Presentation)      :ubi-pres,  after ubi-sub, 2d
    PerCom (Submission)         :per-sub,   2025-12-09, 7d
    PerCom (Review)             :per-rev,   after per-sub, 14d
    PerCom (Presentation)       :per-pres,  after per-rev, 2d

    %% --------------------------
    %% Sensor
    %% --------------------------
    section Sensor
    SenSys* (Submission)        :sens-sub,  2025-07-31, 7d
    SenSys* (Presentation)      :sens-pres, after sens-sub, 2d

    %% --------------------------
    %% Network
    %% --------------------------
    section Network
    NSDI* (Submission)          :nsdi-sub,  2025-04-25, 7d
    NSDI* (Presentation)        :nsdi-pres, after nsdi-sub, 2d
    SIGCOMM* (Submission)       :sig-sub,   2025-10-04, 7d
    SIGCOMM* (Presentation)     :sig-pres,  after sig-sub, 2d
    INFOCOM (Submission)        :info-sub,  2025-07-31, 7d
    INFOCOM (Presentation)      :info-pres, after info-sub, 2d

    %% --------------------------
    %% Operating Systems
    %% --------------------------
    section Operating Systems
    OSDI* (Submission)          :osdi-sub,  2025-12-10, 7d
    OSDI* (Presentation)        :osdi-pres, after osdi-sub, 2d
    SOSP* (Submission)          :sosp-sub,  2025-04-17, 7d
    SOSP* (Presentation)        :sosp-pres, after sosp-sub, 2d
    ATC** (Submission)          :atc-sub,   2025-01-14, 7d
    ATC** (Presentation)        :atc-pres,  after atc-sub, 2d
    EuroSys** (Submission)      :euros-sub, 2025-05-21, 7d
    EuroSys** (Presentation)    :euros-pres,after euros-sub, 2d
    ASPLOS* (Submission)        :aspl-sub,  2025-03-01, 7d
    ASPLOS* (Presentation)      :aspl-pres, after aspl-sub, 2d

    %% --------------------------
    %% Embedded / EDA
    %% --------------------------
    section Embedded / EDA
    EMSOFT* (Submission)        :ems-sub,   2025-08-29, 7d
    EMSOFT* (Presentation)      :ems-pres,  after ems-sub, 2d
    DAC* (Submission)           :dac-sub,   2025-11-19, 7d
    DAC* (Presentation)         :dac-pres,  after dac-sub, 2d
    DATE (Submission)           :date-sub,  2025-09-22, 7d
    DATE (Presentation)         :date-pres, after date-sub, 2d

    %% --------------------------
    %% Multimedia
    %% --------------------------
    section Multimedia
    MM (Submission)             :mm-sub,    2025-04-11, 7d
    MM (Presentation)           :mm-pres,   after mm-sub, 2d


