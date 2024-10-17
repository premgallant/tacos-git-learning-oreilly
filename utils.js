  function getLink(id) {
      const link = document.createElement("a");
      link.href = id; // Set the URL
      link.textContent = "Click here"; // Set the link text
      return link;
    }

    function printuniqaddSet() {
      console.log('---------------------------------\t' + uniq_changes_add.size);
      // Using forEach method
      uniq_changes_add.forEach(value => {
        console.log(value);
      });
      console.log('------------------------------------');

    }
    function printidmapandContent() {

      for (const [key, value] of uniq_changes_map.entries()) {
        console.log(`Key: ${key}, Value: ${value}`);
      }
    }

    function scrollToElement(elementId) {
      const element = document.getElementById(elementId);
      if (element) {
        element.scrollIntoView({
          behavior: 'smooth'
        });
      } else {
        console.error(`Element with ID '${elementId}'   
 not found.`);
      }
    }
