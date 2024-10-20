const { faker } = require('@faker-js/faker');

function generateLoginRecord() {
  const userId = faker.internet.userName();
  const timestamp = faker.date.recent({ days: 30 }).getTime(); 
  const ip = faker.internet.ip();
  const location = faker.location.nearbyGPSCoordinate({ origin: [32.78306, -96.80667], radius: 100 }); // Near Dallas

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
    ip_asn_name: "Ally Financial Inc.", 
    ip_asn_id: "AS54775", 
    os_name: faker.helpers.arrayElement(["Windows", "macOS", "Linux"]),
    os_version: faker.system.semver(),
    browser_name: faker.helpers.arrayElement(["Chrome", "Firefox", "Safari", "Edge"]),
    browser_version: faker.system.semver(),
    user_agent: faker.internet.userAgent(),
    ip_domain: "ally.com", 
    ip_organization_name: "Ally Financial Inc.",
    ip_organization_type: "business",
    ip_location_longitude: location[1], 
    ip_location_latitude: location[0],
    ip_location_region: "Texas", 
    ip_location_city: "Dallas", 
    ip_location_zip: faker.location.zipCode(),
    ip_location_timezone: "America/Chicago", 
    device_platform: faker.helpers.arrayElement(["desktop", "mobile", "tablet"]),
    device_timezone: faker.location.timeZone(),
    device_languages: [
      "en-US",
      "en"
    ]
  };
}


const records = [];
for (let i = 0; i < 5; i++) {
  records.push(generateLoginRecord());
}

console.log(JSON.stringify(records, null, 2)); // Pretty-print the JSON