const { faker } = require('@faker-js/faker');

function generateAccountData() {

  const accountType = faker.helpers.arrayElement(['Checking', 'Savings', 'Credit Card', 'Mortgage', 'Auto', 'Investment']);
  let balance;
  switch (accountType) {
    case 'Mortgage':
      balance = faker.number.float({ min: 250000, max: 300000, precision: 2 }); // Use faker.number.float() with precision
      break;
    case 'Investment':
      balance = faker.number.float({ min: 100000, max: 200000, precision: 2 });
      break;
    case 'Credit Card':
      balance = faker.number.float({ min: 5000, max: 10000, precision: 2 });
      break;
    case 'Savings':
      balance = faker.number.float({ min: 10000, max: 30000, precision: 2 });
      break;
    case 'Checking':
      balance = faker.number.float({ min: 5000, max: 12000, precision: 2 });
      break;
    default: // Auto
      balance = faker.number.float({ min: 10000, max: 50000, precision: 2 }); 
  }
  return {
    accountNumber: faker.finance.accountNumber(),
    balance: balance,
    accountType: accountType,
  };
}

function generateSampleUserData() {
  const userAgent = faker.internet.userAgent();
  const numAccounts = faker.number.int({ min: 1, max: 5 }); // Use faker.number.int()
  const accounts = [];

  for (let i = 0; i < numAccounts; i++) {
    const accountData = generateAccountData();
    const tenYearsAgo = new Date();
    tenYearsAgo.setFullYear(tenYearsAgo.getFullYear() - 10);
    accountData.accountOpenDate = faker.date.between({ from: tenYearsAgo, to: new Date() }); 
    accounts.push(accountData);
  }

  return {
    customerId: faker.string.numeric(10), 
    firstName: faker.person.firstName(),
    lastName: faker.person.lastName(),
    phoneNumber: faker.phone.number(), 
    phoneType: faker.helpers.arrayElement(['Mobile']),
    ipAddress: faker.internet.ip(),
    latitude: faker.location.latitude(),
    longitude: faker.location.longitude(),
    state: faker.location.state(),
    city: faker.location.city(),
    zip: faker.location.zipCode(),
    mobileOS: userAgent.includes('Android') ? 'Android' : (userAgent.includes('iPhone') ? 'iOS' : 'iPadOS'),
    accounts: accounts, // Add the accounts array to the user data
  };
}

// Generate 5 sample user data objects
for (let i = 0; i < 5; i++) {
  console.log(generateSampleUserData());
}