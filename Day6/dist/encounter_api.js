const API_BASE_URL = "http://localhost:8000";
async function errorMessage(response) {
    const body = await response.json().catch(() => null);
    const detail = body?.detail;
    if (Array.isArray(detail))
        return detail.map((d) => `${d.loc?.at(-1)}: ${d.msg}`).join("; ");
    return detail ?? `HTTP error! Status: ${response.status}`;
}
export async function getEncounterById(id) {
    const response = await fetch(`${API_BASE_URL}/encounters/${id}`);
    if (!response.ok) {
        throw new Error(await errorMessage(response));
    }
    const data = await response.json();
    return data;
}
// Latest encounters first (GET /encounters?newest_first=true).
export async function getEncounters(limit = 20) {
    const response = await fetch(`${API_BASE_URL}/encounters?newest_first=true&limit=${limit}`);
    if (!response.ok) {
        throw new Error(await errorMessage(response));
    }
    const data = await response.json();
    return data;
}
export async function createEncounter(encounter) {
    const response = await fetch(`${API_BASE_URL}/encounters`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(encounter),
    });
    if (!response.ok) {
        throw new Error(await errorMessage(response));
    }
    const data = await response.json();
    return data;
}
export async function patchEncounterById(id, updates) {
    const response = await fetch(`${API_BASE_URL}/interventions/${id}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(updates),
    });
    if (!response.ok) {
        throw new Error(await errorMessage(response));
    }
}
