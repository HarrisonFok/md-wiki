import Article from '../../src/views/Article.vue'
import { shallowMount } from '@vue/test-utils';
describe("Article.vue", () => {
    let wrapper;
    it("renders", () => {
        expect(wrapper.exists()).toBe(true)
    })
})