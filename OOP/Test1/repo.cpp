#include "repo.h"
#include "dynamicArray.h"

void repo::add(TElem &elem) {
    repo.add(elem);
}

void repo::remove(TElem &elem) {
    /**
     * simply call the remove from the dynamicArray
     */
    repo.remove(elem);

}
