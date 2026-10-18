
import type { Encounter } from "./encounter_interface";

const API_BASE_URL = "http://localhost:8000";

// Body for POST /encounters: encounter_id is optional (the API generates one).
export type EncounterCreate = Omit<Encounter, "encounter_id"> & { encounter_id?: number };

// What the Python API returns: the stored row plus risk scoring and any queued intervention.
export interface EncounterRecord extends Encounter {
  readmitted: string;
  risk_score: number;
  risk_level: "LOW" | "MEDIUM" | "HIGH";
  intervention_id: number | null;
  intervention_status: string | null;
}

async function errorMessage(response: Response): Promise<string> {
  const body = await response.json().catch(() => null);
  const detail = body?.detail;
  if (Array.isArray(detail)) return detail.map((d) => `${d.loc?.at(-1)}: ${d.msg}`).join("; ");
  return detail ?? `HTTP error! Status: ${response.status}`;
}

export async function getEncounterById(id: number): Promise<EncounterRecord> {
  const response = await fetch(`${API_BASE_URL}/encounters/${id}`);

  if (!response.ok) {
    throw new Error(await errorMessage(response));
  }

  const data: EncounterRecord = await response.json();
  return data;
}

// Latest encounters first (GET /encounters?newest_first=true).
export async function getEncounters(limit = 20): Promise<EncounterRecord[]> {
  const response = await fetch(`${API_BASE_URL}/encounters?newest_first=true&limit=${limit}`);

  if (!response.ok) {
    throw new Error(await errorMessage(response));
  }

  const data: EncounterRecord[] = await response.json();
  return data;
}

export async function createEncounter(encounter: EncounterCreate): Promise<EncounterRecord> {
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

  const data: EncounterRecord = await response.json();
  return data;
}

export async function patchEncounterById(
  id: number,
  updates: Partial<Omit<Encounter, "encounter_id">>,
): Promise<void> {
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
