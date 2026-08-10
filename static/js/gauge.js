/* ==========================================
   TradingBot Executive V8
   Confidence Gauge
========================================== */

function updateGauge(score){

    const fill = document.getElementById("gauge-fill");
    const value = document.getElementById("gauge-value");
    const status = document.getElementById("gauge-status");

    if(!fill || !value || !status) return;

    fill.style.width = score + "%";

    value.innerHTML = score + "%";

    if(score >= 95){

        value.style.color = "#FFD700";
        status.innerHTML = "⭐⭐⭐⭐⭐ EXCELENTE";
        status.style.color = "#FFD700";

    }
    else if(score >= 85){

        value.style.color = "#22c55e";
        status.innerHTML = "MUY ALTA";
        status.style.color = "#22c55e";

    }
    else if(score >= 75){

        value.style.color = "#84cc16";
        status.innerHTML = "ALTA";
        status.style.color = "#84cc16";

    }
    else if(score >= 60){

        value.style.color = "#facc15";
        status.innerHTML = "MODERADA";
        status.style.color = "#facc15";

    }
    else{

        value.style.color = "#ef4444";
        status.innerHTML = "BAJA";
        status.style.color = "#ef4444";

    }

}