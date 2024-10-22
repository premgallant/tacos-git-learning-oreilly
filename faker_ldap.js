const { faker } = require("@faker-js/faker");

function generateUserData() {
  const pwdChangedTime = faker.date.recent({ hours: 24 }).toISOString();
  const mail = faker.internet.email();
  const allyRCpwdHintLastUpdatedTimestamp = faker.date.past().toLocaleString();
  const allyRCpwdLastUpdatedTimestampEpoch = faker.date.past().getTime();
  const allyRCpwdHintLastUpdatedBy = faker.internet.userName();

  return {
    pwdChangedTime: pwdChangedTime,
    allyRCotpDeliveryMethod1: faker.helpers.arrayElement(["EMAIL", "SMS"]),
    allyRCotpDeliveryMethod2: faker.helpers.arrayElement(["EMAIL", "SMS"]),
    mail: mail,
    allyRCnationalIDType: "US SSN",
    allyRCpwdHintLastUpdatedTimestamp: allyRCpwdHintLastUpdatedTimestamp,
    allyRCpasswordHint: null,
    allyRCpasswordAllowChangeTime: "0",
    allyRCuserBlockedFlag: faker.datatype.boolean().toString(),
    allyRCpasswordExpirationTime: "0",
    allyRCpwdHintLastUpdatedBy: allyRCpwdHintLastUpdatedBy,
    allyRCuserLockedFlag: faker.datatype.boolean().toString(),
    allyRCpasswordChange: faker.number.int({ min: 0, max: 1 }).toString(),
    allyRCpwdLastUpdatedTimestamp: allyRCpwdLastUpdatedTimestampEpoch,
    allyRCpasswordMigrationFlag: faker.datatype.boolean().toString(),
  };
}

const records = [];
const numRecords = faker.number.int({ min: 1, max: 10 });

for (let i = 0; i < numRecords; i++) {
  records.push(generateUserData());
}

console.log(JSON.stringify(records, null, 2));
