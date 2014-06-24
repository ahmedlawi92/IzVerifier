from bs4 import BeautifulSoup
from abc import abstractmethod
from IzVerifier.exceptions.IzVerifierException import MissingSpecsException


class IzContainer():
    """
    Abstract class responsible for containing some izpack spec resource.

    For example implementors, see:
    izconditions (for izpack conditions)
    izstrings (for izpack localized strings)
    izvariables (for izpack variables)
    """

    def __init__(self, path):
        self.container = {}
        try:
            self.soup = BeautifulSoup(open(path))
        except IOError:
            raise MissingSpecsException("spec not found at: " + path)
            exit(1)
        self.parse(self.soup)

    @abstractmethod
    def get_keys(self):
        """
        Return all unique keys found for the container's entity.
        """
        pass

    @abstractmethod
    def count(self):
        """
        Return a count of all unique keys found for the container's entity.
        """
        pass

    @abstractmethod
    def has_definition(self, element):
        """
        Return true if the given element contains an izpack definition for the container item.
        """
        pass

    @abstractmethod
    def has_reference(self, element):
        """
        Return true if the given element contains an izpack string reference.
        This method is used to define all the rules that allow the verifier to find
        references to the type of izpack entity being searched for.
        """
        pass

    @abstractmethod
    def get_spec_elements(self):
        """
        Returns a set of the elements defining each of the container's entities.
        """
        pass

    @abstractmethod
    def element_sort_key(self):
        """
        Returns the key to use when sorting elements for this container.
        """
        pass