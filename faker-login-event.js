const { faker } = require("@faker-js/faker");

function generateLoginRecord() {
  const userId = faker.internet.userName();
  // const timestamp = faker.date.recent({ days: 1 }).getTime();
  const timestamp = new Date().getTime(); 
  const ip = faker.internet.ip();
  // Generate random US location data
  const state = faker.location.state();
  const city = faker.location.city();
  const zipCode = faker.location.zipCode(); // Generate a generic zip code for now
  const coordinates = faker.location.nearbyGPSCoordinate({
    origin: [
      faker.location.latitude({ max: 49.3457868, min: 24.7433195 }),
      faker.location.longitude({ max: -66.9513812, min: -124.7844079 }),
    ],
    radius: 100,
  });
  const timeZone = faker.location.timeZone({ region: state });

  return {
    customerId: faker.string.numeric(10),
    action_id: faker.string.uuid(),
    action_performed_at: timestamp,
    action_type: "login",
    device_id: faker.string.uuid(),
    device_fingerprint: faker.string.uuid({ length: 64 }),
    device_public_key: faker.string.uuid({ length: 64 }),
    user_id: userId,
    location: `https://secure-dev.ally.com/`,
    ip: ip,
    ip_country: "US",
    os_name: faker.helpers.arrayElement(["Windows", "macOS", "Linux"]),
    os_version: faker.system.semver(),
    browser_name: faker.helpers.arrayElement([
      "Chrome",
      "Firefox",
      "Safari",
      "Edge",
    ]),
    browser_version: faker.system.semver(),
    user_agent: faker.internet.userAgent(),
    ip_location_longitude: coordinates[1],
    ip_location_latitude: coordinates[0],
    ip_location_region: state, // Use the generated state
    ip_location_city: city,   // Use the generated city
    ip_location_zip: zipCode,
    ip_location_timezone: timeZone,
    device_platform: faker.helpers.arrayElement([
      "desktop",
      "mobile",
      "tablet",
    ]),
    device_timezone: faker.location.timeZone(),
    device_languages: ["en-US", "en"],
  };
}

const records = [];
for (let i = 0; i < 50; i++) {
  records.push(generateLoginRecord());
}

console.log(JSON.stringify(records, null, 2)); // Pretty-print the JSON
