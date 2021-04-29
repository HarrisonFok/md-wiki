import Edit from '../../src/views/Edit.vue'
import { shallowMount } from '@vue/test-utils';
describe("Edit.vue", () => {
    let wrapper;
    beforeEach(() => {
        wrapper = shallowMount(Edit, {
            methods: { getArticles: () => {}, createArticle: () => {}}
        })
    })
    // Make sure that the methods exist
    it("renders", () => {
        expect(wrapper.exists()).toBe(true)
    })
})