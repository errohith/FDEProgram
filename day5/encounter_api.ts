
import type { Encounter } from "./encounter_interface";

async function getEncounterById(id: number): Promise<Encounter> {
  const response = await fetch(`http://localhost:8000/encounters/${id}`);

  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }

  const data: Encounter = await response.json();
  return data;
}

async function patchEncounterById(
  id: number,
  updates: Partial<Omit<Encounter, "encounter_id">>,
): Promise<void> {
  const response = await fetch(`http://localhost:8000/interventions/${id}`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(updates),
  });

  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }
}

async function main() {
  try {
    const data = await getEncounterById(15738);
    console.log(data);
  } catch (error) {
    console.error("Error fetching encounter:", error);
  }
}

main();
