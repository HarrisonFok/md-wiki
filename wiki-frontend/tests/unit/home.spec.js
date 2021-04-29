import Home from '../../src/views/Home.vue'
import { shallowMount } from '@vue/test-utils';
describe("Home.vue", () => {
    let wrapper;
    beforeEach(() => {
        wrapper = shallowMount(Home, {
            methods: { getArticles: () => {}, createArticle: () => {}}
        })
    })
    // Make sure that the methods exist
    it("renders", () => {
        expect(wrapper.exists()).toBe(true)
    })
})